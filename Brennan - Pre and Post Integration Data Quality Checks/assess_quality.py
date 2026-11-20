from pathlib import Path
import re
import sys
import pandas as pd

root = Path(__file__).resolve().parents[1]
processed = root / "data" / "processed"
integrated = root / "data" / "integrated"
reports = root / "reports"
files = {
    "Census ACS": processed / "acs_county_housing_income_2019_2024.csv",
    "BLS LAUS": processed / "bls_county_unemployment_2019_2024.csv",
    "BEA GDP": processed / "bea_county_gdp_2019_2024.csv"
}


def normalized(text):
    return re.sub(r"[^a-z0-9]", "", str(text).lower())


def pick(df, names):
    by_name = {normalized(c): c for c in df.columns}
    for name in names:
        if normalized(name) in by_name:
            return by_name[normalized(name)]
    return None


def valid_fips(value):
    if pd.isna(value):
        return False
    value = str(value).strip().replace(".0", "")
    return bool(re.search(r"\d{5}$", value)) or bool(re.fullmatch(r"\d{1,4}", value))


def as_number(series):
    text = series.astype("string").str.replace(r"[$,%\s]", "", regex=True).str.replace(",", "", regex=False)
    return pd.to_numeric(text, errors="coerce")


def describe(name, path):
    if not path.exists():
        return [f"## {name}", "", f"File not found: `{path.relative_to(root)}`", ""]
    df = pd.read_csv(path, dtype=str, low_memory=False)
    year_col = pick(df, ["year", "report_year", "reporting_year", "acs_year", "period", "time_period"])
    fips_col = pick(df, ["county_fips", "geofips", "geoid", "geo_id", "fips", "fips_code"])
    year_numbers = df[year_col].astype(str).str.extract(r"(20\d{2})(?!.*20\d{2})", expand=False).dropna().astype(int) if year_col else pd.Series(dtype=int)
    duplicate_rows = int(df.duplicated().sum())
    state_col = pick(df, ["state_fips", "statefp", "state"])
    county_col = pick(df, ["county_code", "countyfp", "county"])
    if fips_col and year_col:
        key_duplicates = int(df.duplicated([fips_col, year_col]).sum())
    elif state_col and county_col and year_col:
        key_duplicates = int(df.duplicated([state_col, county_col, year_col]).sum())
    else:
        key_duplicates = None
    blank_cells = int(df.fillna("").apply(lambda col: col.str.strip().eq("")).sum().sum())
    total_cells = df.shape[0] * df.shape[1]
    lines = [f"## {name}", "", f"File: `{path.relative_to(root)}`", "", f"Rows: {len(df):,}; columns: {len(df.columns)}."]
    lines += [f"Completeness: {blank_cells:,} blank cells out of {total_cells:,} ({blank_cells / total_cells * 100:.2f}%)." if total_cells else "Completeness: no records to assess."]
    lines.append(f"Consistency: {duplicate_rows:,} exact duplicate rows.")
    lines.append(f"County-year duplicates: {key_duplicates:,}." if key_duplicates is not None else "County-year duplicates: not checked because the key columns were not identified.")
    if fips_col:
        invalid = int((~df[fips_col].map(valid_fips)).sum())
        lines.append(f"FIPS values that do not look numeric: {invalid:,}.")
    elif state_col and county_col:
        valid_state = df[state_col].astype(str).str.fullmatch(r"\d{1,2}")
        valid_county = df[county_col].astype(str).str.fullmatch(r"\d{1,3}")
        lines.append(f"FIPS components with invalid state/county codes: {int((~(valid_state & valid_county)).sum()):,}.")
    else:
        lines.append("FIPS format: check manually; no standard FIPS column found.")
    if not year_numbers.empty:
        lines.append(f"Timeliness: data years range from {year_numbers.min()} to {year_numbers.max()}.")
    else:
        wide_years = [str(c) for c in df.columns if re.fullmatch(r"20\d{2}", str(c))]
        lines.append(f"Timeliness: year columns range from {min(wide_years)} to {max(wide_years)}." if wide_years else "Timeliness: year range could not be read automatically.")
    checks = [
        (["unemployment_rate", "annual_unemployment_rate", "unemp_rate", "rate"], 0, 100, "unemployment rate"),
        (["median_household_income", "median_income", "b19013_001e"], 0, None, "median income"),
        (["median_home_value", "median_housing_value", "b25077_001e"], 0, None, "home value"),
        (["gdp_current_dollars", "gdp", "county_gdp", "real_gdp", "nominal_gdp", "gdp_thousands"], 0, None, "GDP")
    ]
    checked = 0
    for names, low, high, label in checks:
        col = pick(df, names)
        if not col:
            continue
        checked += 1
        numeric = as_number(df[col])
        invalid = numeric.lt(low) if low is not None else pd.Series(False, index=df.index)
        if high is not None:
            invalid = invalid | numeric.gt(high)
        lines.append(f"Accuracy checks ({label}): {int(invalid.sum()):,} values outside the expected range; {int(numeric.isna().sum()):,} missing or non-numeric values.")
    if not checked:
        lines.append("Accuracy: no standard measurement names found automatically; inspect the columns and source documentation.")
    if name == "BLS LAUS" and all(c in df.columns for c in ["labor_force", "employment", "unemployment", "unemployment_rate"]):
        labor = as_number(df["labor_force"])
        employed = as_number(df["employment"])
        unemployed = as_number(df["unemployment"])
        rate = as_number(df["unemployment_rate"])
        mismatch = (labor - employed - unemployed).abs() > 0.1
        rate_mismatch = ((unemployed / labor * 100) - rate).abs() > 0.11
        lines.append(f"Consistency: {int(mismatch.sum()):,} rows where employment plus unemployment differs from the labor force.")
        lines.append(f"Consistency: {int(rate_mismatch.sum()):,} unemployment rates differ from the component counts by more than 0.11 percentage points.")
    missing_by_col = df.isna().sum().sort_values(ascending=False)
    top = missing_by_col[missing_by_col > 0].head(5)
    if len(top):
        lines.append("Most missing fields: " + ", ".join(f"{c} ({int(v):,})" for c, v in top.items()) + ".")
    lines.extend(["", "These checks can identify possible errors but cannot prove accuracy. Source comparisons and explanations for changes are still needed.", ""])
    return lines


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "before"
    if stage not in ("before", "after"):
        raise ValueError("Use 'before' or 'after'")
    reports.mkdir(exist_ok=True)
    if stage == "before":
        heading = "# Pre-Integration Data Quality Assessment\n\nThis assessment checks the processed source files before they are joined. It does not replace assessment of the original raw downloads.\n"
        lines = [heading]
        for name, path in files.items():
            lines.extend(describe(name, path))
        output = reports / "pre_integration_quality.md"
    else:
        heading = "# Post-Integration Data Quality Assessment\n\nThis assessment checks the merged data for missingness, validity, and duplicate county-year keys. Compare it with the original datasets and the integration summary.\n"
        lines = [heading]
        lines.extend(describe("Integrated Census, BLS and BEA", integrated / "housing_county_2019_2024.csv"))
        output = reports / "post_integration_quality.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()

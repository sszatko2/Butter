from pathlib import Path
import re
import pandas as pd

root = Path(__file__).resolve().parents[1]
source_dir = root / "data" / "processed"
output_dir = root / "data" / "integrated"
report_dir = root / "reports"

files = {
    "acs": "acs_county_housing_income_2019_2024.csv",
    "bls": "bls_county_unemployment_2019_2024.csv",
    "bea": "bea_county_gdp_2019_2024.csv"
}


def normalize(value):
    return re.sub(r"[^a-z0-9]", "", str(value).lower())


def find_column(df, names):
    lookup = {normalize(c): c for c in df.columns}
    for name in names:
        if normalize(name) in lookup:
            return lookup[normalize(name)]
    return None


def clean_fips(value):
    if pd.isna(value):
        return None
    text = str(value).strip().strip('"').replace(".0", "")
    match = re.search(r"(?:US)?(\d{5})$", text)
    if match:
        return match.group(1)
    if text.isdigit() and len(text) <= 5:
        return text.zfill(5)
    return None


def add_fips(df, name):
    fips_col = find_column(df, ["county_fips", "geofips", "geoid", "geo_id", "fips", "fips_code", "county_code_fips", "countyid"])
    state_col = find_column(df, ["state_fips", "state_code", "statefp", "state"])
    county_col = find_column(df, ["county_code", "countyfp", "county"])
    if fips_col:
        df["county_fips"] = df[fips_col].map(clean_fips)
        if state_col and county_col:
            state = df[state_col].astype(str).str.extract(r"(\d{1,2})", expand=False).str.zfill(2)
            county = df[county_col].astype(str).str.extract(r"(\d{1,3})", expand=False).str.zfill(3)
            combined = state + county
            original = df[fips_col].astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
            df.loc[original.str.fullmatch(r"\d{1,3}").fillna(False), "county_fips"] = combined
    elif state_col and county_col:
        state = df[state_col].astype(str).str.extract(r"(\d{1,2})", expand=False).str.zfill(2)
        county = df[county_col].astype(str).str.extract(r"(\d{1,3})", expand=False).str.zfill(3)
        df["county_fips"] = (state + county).where(state.notna() & county.notna())
    else:
        raise ValueError(f"{name}: Could not find a county FIPS column. Columns: {list(df.columns)}")
    return df


def add_year(df, name):
    year_col = find_column(df, ["year", "report_year", "reporting_year", "acs_year", "period", "time_period", "date"])
    if year_col:
        df["year"] = pd.to_numeric(df[year_col].astype(str).str.extract(r"(20\d{2})(?!.*20\d{2})", expand=False), errors="coerce")
        return df
    years = [c for c in df.columns if re.fullmatch(r"20\d{2}", str(c).strip())]
    if years:
        df = df.melt(id_vars=[c for c in df.columns if c not in years], value_vars=years, var_name="year", value_name="year_value")
        df["year"] = pd.to_numeric(df["year"], errors="coerce")
        return df
    raise ValueError(f"{name}: Could not find a year column. Columns: {list(df.columns)}")


def find_value_column(df, options, name):
    col = find_column(df, options)
    if col:
        return col
    candidates = [c for c in df.columns if "gdp" in normalize(c) and "growth" not in normalize(c) and "percapita" not in normalize(c)] if name == "bea" else []
    if len(candidates) == 1:
        return candidates[0]
    if "year_value" in df.columns and name == "bea":
        return "year_value"
    raise ValueError(f"{name}: Could not identify the value column. Columns: {list(df.columns)}")


def to_number(series):
    values = series.astype("string").str.replace(r"[$,%\s]", "", regex=True).str.replace(",", "", regex=False)
    values = values.str.replace(r"^\((\d+(?:\.\d+)?)\)$", r"-\1", regex=True)
    numbers = pd.to_numeric(values, errors="coerce")
    return numbers.mask(numbers <= -666666666)


def load_source(name):
    path = source_dir / files[name]
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Put Samantha's processed CSVs in data/processed/ first.")
    df = pd.read_csv(path, dtype=str, low_memory=False)
    df = add_year(add_fips(df, name), name)
    df = df.dropna(subset=["county_fips", "year"]).copy()
    df["year"] = df["year"].astype(int)
    if name == "acs":
        values = {
            "median_household_income": ["median_household_income", "median_income", "household_income", "b19013_001e", "b19013001e"],
            "median_home_value": ["median_home_value", "median_housing_value", "median_house_price", "median_household_value", "median_owner_occupied_home_value", "b25077_001e", "b25077001e"]
        }
    elif name == "bls":
        values = {"unemployment_rate": ["unemployment_rate", "annual_unemployment_rate", "annual_avg_unemployment_rate", "unemploymentrate", "unemp_rate", "rate"]}
    else:
        values = {"gdp": ["gdp", "county_gdp", "real_gdp", "realgdp", "nominal_gdp", "gdp_current_dollars", "gdp_millions", "gross_domestic_product", "year_value"]}
    result = df[["county_fips", "year"]].copy()
    if name == "acs":
        place = find_column(df, ["name", "county_name", "geoname", "area_name"])
        if place:
            result["county_name"] = df[place]
    for target, options in values.items():
        column = find_value_column(df, options, name)
        result[target] = to_number(df[column])
        result.loc[result[target] < 0, target] = pd.NA
    duplicates = result.duplicated(["county_fips", "year"], keep=False)
    if duplicates.any():
        sample = result.loc[duplicates, ["county_fips", "year"]].head(6).to_dict("records")
        raise ValueError(f"{name}: Duplicate county-year records found. Check whether your CSV has multiple data types per county/year: {sample}")
    return result


def main():
    tables = {name: load_source(name) for name in files}
    keys = {name: set(zip(table["county_fips"], table["year"])) for name, table in tables.items()}
    common = keys["acs"] & keys["bls"] & keys["bea"]
    merged = tables["acs"].merge(tables["bls"], on=["county_fips", "year"], how="inner", validate="one_to_one")
    merged = merged.merge(tables["bea"], on=["county_fips", "year"], how="inner", validate="one_to_one")
    if merged.empty:
        raise ValueError("No matching county-year records across all three datasets. Check year ranges and FIPS columns.")
    merged["home_value_to_income_ratio"] = merged["median_home_value"].div(merged["median_household_income"].replace(0, pd.NA))
    merged = merged.sort_values(["year", "county_fips"])
    output_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    merged.to_csv(output_dir / "housing_county_2019_2024.csv", index=False)
    lines = [
        "# Data Integration Summary", "",
        "The three processed datasets were joined using county FIPS codes and the year associated with each record.",
        "Only county-year combinations found in all three datasets were kept.", "",
        "| Dataset | County-year records | Matched across all 3 | Not matched |",
        "|---|---:|---:|---:|"
    ]
    for name in files:
        lines.append(f"| {name.upper()} | {len(keys[name])} | {len(common)} | {len(keys[name] - common)} |")
    lines.extend(["", "| Year | Matched county-year records |", "|---|---:|"])
    for year, count in merged.groupby("year").size().items():
        lines.append(f"| {year} | {count:,} |")
    lines += [
        "", f"Integrated records: {len(merged):,}",
        f"Years in merged data: {', '.join(map(str, sorted(merged['year'].unique())))}", "",
        "The ACS estimates cover five-year windows ending in the labeled year. BLS and BEA values are annual, so matching on year does not make their time periods identical.",
        "The GDP column uses BEA current-dollar GDP from gdp_current_dollars in the processed source file (dollars, not thousands).",
        "Rows with missing numeric measurements are kept so missingness can be assessed after joining."
    ]
    (report_dir / "integration_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Saved {len(merged):,} merged rows to {output_dir / 'housing_county_2019_2024.csv'}")


if __name__ == "__main__":
    main()

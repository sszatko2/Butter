from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
raw_dir = root / "data" / "raw"
processed = root / "data" / "processed"
reports = root / "reports"
sources = {
    "acs": "acs_county_housing_income_2019_2024.csv",
    "bls": "bls_county_unemployment_2019_2024.csv",
    "bea": "bea_county_gdp_2019_2024.csv"
}


def find_raw(name):
    if not raw_dir.exists():
        return None
    matches = sorted([p for p in raw_dir.glob("*.csv") if name.lower() in p.name.lower()])
    return matches[0] if len(matches) == 1 else None


def main():
    reports.mkdir(exist_ok=True)
    lines = ["# Cleaning Verification", "", "This review checks the processed files and identifies where the original raw files or notebook steps still need to be verified.", ""]
    for name, filename in sources.items():
        lines += [f"## {name.upper()}", ""]
        path = processed / filename
        if not path.exists():
            lines += [f"Processed file missing: `{path.relative_to(root)}`", ""]
            continue
        clean = pd.read_csv(path, dtype=str, low_memory=False)
        lines += [f"Processed file: `{path.relative_to(root)}`", f"Processed rows: {len(clean):,}; columns: {len(clean.columns)}.", f"Exact duplicate rows: {int(clean.duplicated().sum()):,}."]
        blanks = int(clean.isna().sum().sum())
        lines.append(f"Missing values in processed file: {blanks:,}.")
        if name == "acs":
            value = pd.to_numeric(clean["median_home_value"], errors="coerce")
            income = pd.to_numeric(clean["median_household_income"], errors="coerce")
            recorded = pd.to_numeric(clean["home_value_income_ratio"], errors="coerce")
            expected = value / income.replace(0, float("nan"))
            mismatch = (expected - recorded).abs().gt(0.000001)
            lines.append(f"Affordability ratio mismatches (among available values): {int(mismatch.sum()):,}.")
        elif name == "bls":
            labor = pd.to_numeric(clean["labor_force"], errors="coerce")
            employment = pd.to_numeric(clean["employment"], errors="coerce")
            unemployment = pd.to_numeric(clean["unemployment"], errors="coerce")
            rate = pd.to_numeric(clean["unemployment_rate"], errors="coerce")
            total_mismatch = (labor - employment - unemployment).abs().gt(0.1)
            rate_mismatch = (unemployment / labor * 100 - rate).abs().gt(0.11)
            lines.append(f"Labor force total mismatches: {int(total_mismatch.sum()):,}.")
            lines.append(f"Unemployment rate mismatches beyond rounding: {int(rate_mismatch.sum()):,}.")
        elif name == "bea":
            thousands = pd.to_numeric(clean["gdp_thousands"], errors="coerce")
            dollars = pd.to_numeric(clean["gdp_current_dollars"], errors="coerce")
            mismatch = (thousands * 1000 - dollars).abs().gt(0.01)
            lines.append(f"GDP conversion mismatches (thousands to dollars): {int(mismatch.sum()):,}.")
        raw_path = find_raw(name)
        if raw_path:
            raw = pd.read_csv(raw_path, dtype=str, low_memory=False)
            lines += [f"Raw file used for comparison: `{raw_path.relative_to(root)}`", f"Raw rows: {len(raw):,}; columns: {len(raw.columns)}.", f"Difference in row count (processed minus raw): {len(clean) - len(raw):,}."]
            shared = sorted(set(raw.columns) & set(clean.columns))
            lines.append(f"Shared column names: {len(shared)}. Changed row counts do not by themselves prove cleaning is correct.")
        else:
            lines.append("Raw CSV not found automatically in `data/raw/`. Original-to-cleaned changes still need to be checked using the source download and the cleaning notebook.")
        notebooks = sorted((root / "data_cleaning_files").glob(f"*{name}*.ipynb")) if (root / "data_cleaning_files").exists() else []
        lines.append("Cleaning notebook: " + ", ".join(f"`{p.relative_to(root)}`" for p in notebooks) if notebooks else "Cleaning notebook not found automatically. Check the repository file names.")
        lines += [""]
    lines += ["## Follow-up", "", "For each source, document the original download URL, any renamed columns, converted types, dropped records, and missing-value decisions. Verify that running the notebook or an equivalent script reproduces the processed CSV. The current checks do not establish this on their own.", ""]
    output = reports / "cleaning_verification.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()

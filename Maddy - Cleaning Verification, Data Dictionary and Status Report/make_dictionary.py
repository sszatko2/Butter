from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
data = root / "data" / "integrated" / "housing_county_2019_2024.csv"
docs = root / "docs"
meanings = {
    "county_fips": "Five-digit county FIPS identifier used to join datasets",
    "year": "Reporting year; ACS estimates cover the five-year period ending in this year",
    "county_name": "County name supplied by the Census source",
    "median_household_income": "Median annual household income from ACS, in US dollars",
    "median_home_value": "Median value of owner-occupied homes from ACS, in US dollars",
    "unemployment_rate": "BLS county unemployment rate, percent",
    "gdp": "County gross domestic product from BEA; verify the unit and whether values are real or current-dollar",
    "home_value_to_income_ratio": "Median home value divided by median household income"
}


def main():
    if not data.exists():
        raise FileNotFoundError("Run the integration script before creating the data dictionary")
    df = pd.read_csv(data, dtype={"county_fips": str})
    docs.mkdir(exist_ok=True)
    lines = ["# Data Dictionary", "", "Dataset: `data/integrated/housing_county_2019_2024.csv`", "", "| Column | Data type | Description | Missing rows |", "|---|---|---|---:|"]
    for col in df.columns:
        desc = meanings.get(col, "Review source data documentation for definition")
        lines.append(f"| {col} | {df[col].dtype} | {desc} | {int(df[col].isna().sum()):,} |")
    lines += ["", "The source of each value is Census ACS (housing and income), BLS LAUS (unemployment), or BEA (GDP). County FIPS and year are the common keys.", ""]
    (docs / "data_dictionary.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {docs / 'data_dictionary.md'}")


if __name__ == "__main__":
    main()

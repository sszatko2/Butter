from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
processed = root / "data" / "processed"
merged_file = root / "data" / "integrated" / "housing_county_2019_2024.csv"


def read(name):
    return pd.read_csv(processed / name, dtype={"county_fips": str})


def main():
    acs = read("acs_county_housing_income_2019_2024.csv")
    bls = read("bls_county_unemployment_2019_2024.csv")
    bea = read("bea_county_gdp_2019_2024.csv")
    merged = pd.read_csv(merged_file, dtype={"county_fips": str})
    sources = [acs, bls, bea]
    for source in sources + [merged]:
        if source.duplicated(["county_fips", "year"]).any():
            raise ValueError("Duplicate county-year records found")
    keys = [set(zip(source["county_fips"], source["year"])) for source in sources]
    expected_keys = keys[0] & keys[1] & keys[2]
    actual_keys = set(zip(merged["county_fips"], merged["year"]))
    if actual_keys != expected_keys:
        raise ValueError("Integrated county-year keys do not match the common source keys")
    with_bea = merged.merge(bea[["county_fips", "year", "gdp_current_dollars"]], on=["county_fips", "year"])
    bad_gdp = (with_bea["gdp"] - with_bea["gdp_current_dollars"]).abs().gt(0.01)
    if bad_gdp.any():
        raise ValueError(f"BEA GDP mismatch for {bad_gdp.sum()} rows")
    with_acs = merged.merge(acs[["county_fips", "year", "home_value_income_ratio"]], on=["county_fips", "year"])
    bad_ratio = (with_acs["home_value_to_income_ratio"] - with_acs["home_value_income_ratio"]).abs().gt(0.000001)
    if bad_ratio.any():
        raise ValueError(f"Housing ratio mismatch for {bad_ratio.sum()} rows")
    print(f"Integration checks passed: {len(merged):,} matched county-year rows across 2019-2024")


if __name__ == "__main__":
    main()

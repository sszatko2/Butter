from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
input_file = root / "data" / "integrated" / "housing_county_2019_2024.csv"
result_dir = root / "results"


def main():
    if not input_file.exists():
        raise FileNotFoundError("Run integrate_data.py before analyze_data.py")
    df = pd.read_csv(input_file, dtype={"county_fips": str})
    df = df.replace([float("inf"), -float("inf")], pd.NA)
    result_dir.mkdir(exist_ok=True)
    usable = df.dropna(subset=["median_household_income", "median_home_value", "home_value_to_income_ratio"])
    usable = usable[usable["median_household_income"] > 0]
    if usable.empty:
        raise ValueError("No rows with valid home values and income for analysis")
    latest = int(usable["year"].max())
    current = usable[usable["year"] == latest].copy()
    current.sort_values("home_value_to_income_ratio", ascending=False).head(20).to_csv(result_dir / "top_20_housing_ratios.csv", index=False)
    summary = current[["median_home_value", "median_household_income", "home_value_to_income_ratio", "unemployment_rate", "gdp"]].describe()
    summary.to_csv(result_dir / "housing_summary.csv")
    plot = current.dropna(subset=["unemployment_rate", "home_value_to_income_ratio"])
    if not plot.empty:
        plt.figure(figsize=(7, 5))
        plt.scatter(plot["unemployment_rate"], plot["home_value_to_income_ratio"], alpha=0.4)
        plt.xlabel("Unemployment rate (%)")
        plt.ylabel("Home value / household income")
        plt.title(f"County housing affordability and unemployment, {latest}")
        plt.tight_layout()
        plt.savefig(result_dir / "housing_vs_unemployment.png", dpi=150)
        plt.close()
    correlation = plot["unemployment_rate"].corr(plot["home_value_to_income_ratio"])
    median_ratio = current["home_value_to_income_ratio"].median()
    (result_dir / "analysis_notes.md").write_text(
        f"# Initial Analysis\n\nLatest shared reporting year: {latest}.\n\n"
        f"Counties with usable housing values and incomes: {len(current):,}.\n\n"
        f"Median home-value-to-income ratio: {median_ratio:.3f}.\n\n"
        f"Correlation of unemployment and home-value-to-income ratio (counties with both): {correlation:.3f}.\n\n"
        "The home-value-to-income ratio compares median owner-occupied home value to median household income. "
        "A higher ratio suggests less affordability by this simple measure, but it does not represent a mortgage payment or local rent. "
        "These associations should not be interpreted as causation.\n",
        encoding="utf-8"
    )
    print(f"Saved initial results for {latest} to {result_dir}")


if __name__ == "__main__":
    main()

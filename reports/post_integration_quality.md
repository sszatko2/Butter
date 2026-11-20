# Post-Integration Data Quality Assessment

This assessment checks the merged data for missingness, validity, and duplicate county-year keys. Compare it with the original datasets and the integration summary.

## Integrated Census, BLS and BEA

File: `data/integrated/housing_county_2019_2024.csv`

Rows: 18,518; columns: 8.
Completeness: 64 blank cells out of 148,144 (0.04%).
Consistency: 0 exact duplicate rows.
County-year duplicates: 0.
FIPS values that do not look numeric: 0.
Timeliness: data years range from 2019 to 2024.
Accuracy checks (unemployment rate): 0 values outside the expected range; 0 missing or non-numeric values.
Accuracy checks (median income): 0 values outside the expected range; 6 missing or non-numeric values.
Accuracy checks (home value): 0 values outside the expected range; 18 missing or non-numeric values.
Accuracy checks (GDP): 0 values outside the expected range; 18 missing or non-numeric values.
Most missing fields: home_value_to_income_ratio (22), median_home_value (18), gdp (18), median_household_income (6).

These checks can identify possible errors but cannot prove accuracy. Source comparisons and explanations for changes are still needed.


# Pre-Integration Data Quality Assessment

This assessment checks the processed source files before they are joined. It does not replace assessment of the original raw downloads.

## Census ACS

File: `data/processed/acs_county_housing_income_2019_2024.csv`

Rows: 19,328; columns: 7.
Completeness: 107 blank cells out of 135,296 (0.08%).
Consistency: 0 exact duplicate rows.
County-year duplicates: 0.
FIPS values that do not look numeric: 0.
Timeliness: data years range from 2019 to 2024.
Accuracy checks (median income): 0 values outside the expected range; 6 missing or non-numeric values.
Accuracy checks (home value): 0 values outside the expected range; 24 missing or non-numeric values.
Most missing fields: median_gross_rent (49), home_value_income_ratio (28), median_home_value (24), median_household_income (6).

These checks can identify possible errors but cannot prove accuracy. Source comparisons and explanations for changes are still needed.

## BLS LAUS

File: `data/processed/bls_county_unemployment_2019_2024.csv`

Rows: 18,857; columns: 6.
Completeness: 0 blank cells out of 113,142 (0.00%).
Consistency: 0 exact duplicate rows.
County-year duplicates: 0.
FIPS values that do not look numeric: 0.
Timeliness: data years range from 2019 to 2024.
Accuracy checks (unemployment rate): 0 values outside the expected range; 0 missing or non-numeric values.
Consistency: 0 rows where employment plus unemployment differs from the labor force.
Consistency: 0 unemployment rates differ from the component counts by more than 0.11 percentage points.

These checks can identify possible errors but cannot prove accuracy. Source comparisons and explanations for changes are still needed.

## BEA GDP

File: `data/processed/bea_county_gdp_2019_2024.csv`

Rows: 18,762; columns: 5.
Completeness: 156 blank cells out of 93,810 (0.17%).
Consistency: 0 exact duplicate rows.
County-year duplicates: 0.
FIPS values that do not look numeric: 0.
Timeliness: data years range from 2019 to 2024.
Accuracy checks (GDP): 0 values outside the expected range; 78 missing or non-numeric values.
Most missing fields: gdp_current_dollars (78), gdp_thousands (78).

These checks can identify possible errors but cannot prove accuracy. Source comparisons and explanations for changes are still needed.


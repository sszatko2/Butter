# Data Dictionary

Dataset: `data/integrated/housing_county_2019_2024.csv`

| Column | Data type | Description | Missing rows |
|---|---|---|---:|
| county_fips | object | Five-digit county FIPS identifier used to join datasets | 0 |
| year | int64 | Reporting year; ACS estimates cover the five-year period ending in this year | 0 |
| county_name | object | County name supplied by the Census source | 0 |
| median_household_income | float64 | Median annual household income from ACS, in US dollars | 6 |
| median_home_value | float64 | Median value of owner-occupied homes from ACS, in US dollars | 18 |
| unemployment_rate | float64 | BLS county unemployment rate, percent | 0 |
| gdp | float64 | County gross domestic product from BEA; verify the unit and whether values are real or current-dollar | 18 |
| home_value_to_income_ratio | float64 | Median home value divided by median household income | 22 |

The source of each value is Census ACS (housing and income), BLS LAUS (unemployment), or BEA (GDP). County FIPS and year are the common keys.

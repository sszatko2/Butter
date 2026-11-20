# Cleaning Verification

This review checks the processed files and identifies where the original raw files or notebook steps still need to be verified.

## ACS

Processed file: `data/processed/acs_county_housing_income_2019_2024.csv`
Processed rows: 19,328; columns: 7.
Exact duplicate rows: 0.
Missing values in processed file: 107.
Affordability ratio mismatches (among available values): 0.
Raw CSV not found automatically in `data/raw/`. Original-to-cleaned changes still need to be checked using the source download and the cleaning notebook.
Cleaning notebook: `data_cleaning_files/acs_cleaning.ipynb`

## BLS

Processed file: `data/processed/bls_county_unemployment_2019_2024.csv`
Processed rows: 18,857; columns: 6.
Exact duplicate rows: 0.
Missing values in processed file: 0.
Labor force total mismatches: 0.
Unemployment rate mismatches beyond rounding: 0.
Raw CSV not found automatically in `data/raw/`. Original-to-cleaned changes still need to be checked using the source download and the cleaning notebook.
Cleaning notebook: `data_cleaning_files/bls_cleaning.ipynb`

## BEA

Processed file: `data/processed/bea_county_gdp_2019_2024.csv`
Processed rows: 18,762; columns: 5.
Exact duplicate rows: 0.
Missing values in processed file: 156.
GDP conversion mismatches (thousands to dollars): 0.
Raw CSV not found automatically in `data/raw/`. Original-to-cleaned changes still need to be checked using the source download and the cleaning notebook.
Cleaning notebook: `data_cleaning_files/bea_cleaning.ipynb`

## Follow-up

For each source, document the original download URL, any renamed columns, converted types, dropped records, and missing-value decisions. Verify that running the notebook or an equivalent script reproduces the processed CSV. The current checks do not establish this on their own.

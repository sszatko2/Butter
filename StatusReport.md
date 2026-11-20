# Housing Affordability in the United States: Interim Status Report

**IS 477 — Milestone 3**  
**Status date:** November 19, 2026

## Project Progress

Our project examines how housing affordability differs across U.S. counties and how it relates to unemployment and economic output. We are following the USGS Science Data Lifecycle Model and using three sources: Census American Community Survey (ACS) housing and income estimates, Bureau of Labor Statistics (BLS) Local Area Unemployment Statistics, and Bureau of Economic Analysis (BEA) county GDP estimates.

Three county-level datasets have been downloaded, prepared, and added to the repository: [ACS housing and income](data/processed/acs_county_housing_income_2019_2024.csv), [BLS unemployment](data/processed/bls_county_unemployment_2019_2024.csv), and [BEA GDP](data/processed/bea_county_gdp_2019_2024.csv). The files contain 19,328, 18,857, and 18,762 records, respectively, spanning 2019–2024. The repository also contains [cleaning notebooks](data_cleaning_files/), and the agencies' data-use guidance is summarized in the [README](README.md). An initial data profile has been started, but the final version still needs more detail.

Additional scripts and reports have been prepared and tested locally using these processed files. A join using five-digit county FIPS codes and reporting year produced **18,518 matched county-year records**. The integration excluded 810 ACS, 339 BLS, and 244 BEA keys that were not shared across all three sources. No duplicate county-year keys were found in the integrated result. The quality checks identified 22 missing home-value-to-income ratios; these records were retained rather than silently removed. Independent checks found no discrepancies in the available affordability-ratio calculations or the BEA current-dollar GDP values. The output files are listed below and must be committed with this report for the relative links to work:

- [Integration script](Aidan%20-%20County%20Data%20Integration%2C%20Testing%20and%20Workflow/integrate_data.py), [merged CSV](data/integrated/housing_county_2019_2024.csv), and [integration summary](reports/integration_summary.md)
- [Quality assessment script](Brennan%20-%20Pre%20and%20Post%20Integration%20Data%20Quality%20Checks/assess_quality.py), [pre-integration report](reports/pre_integration_quality.md), and [post-integration report](reports/post_integration_quality.md)
- [Cleaning verification](reports/cleaning_verification.md), [data dictionary](docs/data_dictionary.md), [run-all script](Aidan%20-%20County%20Data%20Integration%2C%20Testing%20and%20Workflow/run_pipeline.py), and [initial analysis](results/analysis_notes.md)

These checks establish that the **processed-data** pipeline runs with the available files. They do not yet establish that the original raw downloads and cleaning can be reproduced from start to finish. The raw source files used for the cleaning notebooks are not all included in the repository.

## Updated Timeline and Task Status

The following table updates every task from our original project plan. Dates for unfinished tasks are working targets, subject to the final deadline listed in Canvas.

| Task | Work from original plan | Current status | Lead | Updated target |
|---|---|---|---|---|
| 1 | Choose a lifecycle model | Complete: USGS model | Brennan | Completed |
| 2 | Identify three datasets | Complete: ACS, BLS, BEA | Madelyn | Completed |
| 3 | Submit project plan | Complete | Aidan | Completed |
| 4 | Organize data storage | Partial: processed folders exist; document structure | Brennan | Nov. 23 |
| 5 | Acquire datasets | Processed datasets available; raw acquisition not fully reproducible | Madelyn | Nov. 27 |
| 6 | Review ethical data use | Source guidance reviewed; check final citations and terms | Aidan | Nov. 23 |
| 7 | Draft data profile | Initial draft; needs completion | Samantha | Nov. 25 |
| 8 | Pre-integration quality assessment | Tested on processed files; raw-data review remains | Brennan | Nov. 24 |
| 9 | Clean datasets | Processed files available; source-to-output reproducibility remains | Madelyn | Nov. 27 |
| 10 | Document cleaning | Notebooks exist; link issues to specific cleaning steps | Aidan | Nov. 27 |
| 11 | Integrate three datasets | Local join tested; commit and review output | Aidan* | Nov. 19 |
| 12 | Post-integration assessment | Local checks produced; review and document findings | Brennan | Nov. 23 |
| 13 | Write data quality section | Initial reports available; final narrative remains | Aidan | Nov. 29 |
| 14 | Submit interim status report | Draft finalized; GitHub release and Canvas submission pending | Madelyn | Nov. 19 |
| 15 | Automate workflow | Processed-data run-all script tested; raw stages missing | Aidan* | Nov. 29 |
| 16 | Analyze data | Initial results generated; interpretation still under review | Brennan | Dec. 1 |
| 17 | Create visualizations | Initial plot produced; review labels and findings | Madelyn | Dec. 1 |
| 18 | Write findings and future work | Not started in final-report form | Aidan | Dec. 3 |
| 19 | Write challenges section | Issues identified; expand for final report | Samantha | Dec. 3 |
| 20 | Write reproduction instructions | Partial for processed pipeline; full guide pending | Brennan | Dec. 4 |
| 21 | Metadata and data documentation | Initial data dictionary; structured metadata pending | Madelyn | Dec. 4 |
| 22 | Write final summary | Not started | Aidan | Before final deadline |
| 23 | Revise final report | Not started | Samantha | Before final deadline |
| 24 | Submit final report | Not started | Brennan | Canvas final deadline |

*Tasks 11 and 15 have been reassigned to the integration and workflow lead to align with the roles outlined in the project plan. The data sourcing and preparation steps remain documented in the repository.*

## Changes to the Project Plan

**No instructor feedback was received on Milestone 2**, so there are no instructor-requested revisions to report. Our changes are based on what we learned while preparing and testing the datasets. We expanded the initial 2020–2024 scope to include 2019, since the processed files cover 2019–2024. We also confirmed a working definition of housing affordability: median owner-occupied home value divided by median household income. This is a simple comparison measure, not a full estimate of monthly housing costs.

The original timeline was too optimistic about the time needed to collect, verify, and document the data. We have moved some quality, automation, and reporting work to later dates and clarified responsibility for integration and workflow automation. Our research questions and three primary data sources have not changed. We will update `ProjectPlan.md` to reflect these adjustments. We also plan to use time during fall break to make progress on the remaining work.

## Challenges and Next Steps

The biggest issue is **reproducibility**. We have cleaned CSVs and notebooks, but the complete process of acquiring the raw ACS, BLS, and BEA files and recreating the cleaned datasets has not yet been verified. We plan to document source URLs and checksums, save or provide access to original files, and connect separate acquisition, cleaning, assessment, integration, and analysis scripts in a single workflow. We will then test it from a fresh repository copy.

A second challenge is integrating datasets with different coverage. Matching county FIPS codes and year gave 18,518 shared records, but some county-year combinations were not common to all three files. We used five-character FIPS strings to preserve leading zeros, checked for duplicate join keys, and documented unmatched counts. Missing measurements remain visible for quality assessment rather than being silently filled in.

The datasets also use different reporting periods. ACS five-year estimates are labeled by the final year of a rolling period, while BLS unemployment and BEA GDP are annual statistics. We can match their year labels, but we cannot treat the observations as if they describe identical time windows. We will explain this limitation and avoid interpreting correlations as proof of causation.

Finally, the tested quality reports cover **accuracy checks, completeness, timeliness, and consistency**, but these checks are not proof that the original source values are correct. Before the final submission we need to strengthen raw-to-cleaned validation, finish the data profile and metadata, review the initial graph and findings, and document the complete workflow and its dependencies.

## Individual Contribution Summaries

### Brennan Ryan


### Madelyn McNamara


### Aidan Flaherty

Aidan's assigned work involved combining the three datasets and setting up the workflow. The `integrate_data.py` script matches records using county FIPS codes and years, resulting in 18,518 matched county-year records. The `test_integration.py` script checks the merged data, while `run_pipeline.py` runs the processing steps in order. The `analyze_data.py` script calculates housing affordability ratios and creates an initial graph. The details of the merge are recorded in `reports/integration_summary.md`.

### Samantha Szatko

I downloaded and processed the Bureau of Labor Statistics (BLS), Local Area Unemployment Statistics (LAUS), Bureau of Economic Analysis (BEA) County GDP, and U.S. Census Bureau American Community Survey (ACS) datasets. I cleaned and organized the raw data into CSV format for each dataset and uploaded the processed files into our GitHub repository. I also conducted analysis for ethical data handling by reviewing each sources’ data-use policies and identified relevant considerations related to privacy, copyright, attribution, and data redistribution, all of which will be addressed in our project’s final report. I also drafted the Data Profile section for the final report. 




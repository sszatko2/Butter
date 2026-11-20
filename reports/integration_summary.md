# Data Integration Summary

The three processed datasets were joined using county FIPS codes and the year associated with each record.
Only county-year combinations found in all three datasets were kept.

| Dataset | County-year records | Matched across all 3 | Not matched |
|---|---:|---:|---:|
| ACS | 19328 | 18518 | 810 |
| BLS | 18857 | 18518 | 339 |
| BEA | 18762 | 18518 | 244 |

| Year | Matched county-year records |
|---|---:|
| 2019 | 3,081 |
| 2020 | 3,082 |
| 2021 | 3,082 |
| 2022 | 3,091 |
| 2023 | 3,091 |
| 2024 | 3,091 |

Integrated records: 18,518
Years in merged data: 2019, 2020, 2021, 2022, 2023, 2024

The ACS estimates cover five-year windows ending in the labeled year. BLS and BEA values are annual, so matching on year does not make their time periods identical.
The GDP column uses BEA current-dollar GDP from gdp_current_dollars in the processed source file (dollars, not thousands).
Rows with missing numeric measurements are kept so missingness can be assessed after joining.

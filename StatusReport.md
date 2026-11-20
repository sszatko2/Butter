## Task Update

We have successfully downloaded, cleaned, and prepared the three datasets that we will be using to our research questions pertaining to housing affordability in the United States. All three of the processed datasets have been saved as CSV files and uploaded to our team’s GitHub repository. 

For the Bureau of Labor Statistics (BLS), Local Area Unemployment Statistics (LAUS) dataset, we extracted county-level unemployment data within the timeframe of 2019-2024, standardized geographic identifiers, and organized the relevant unemployment measures into a consistent format. The cleaned dataset is available in our [GitHub repository.](https://github.com/sszatko2/Butter/blob/main/data/processed/bls_county_unemployment_2019_2024.csv)

For the Bureau of Economic Analysis (BEA) County GDP dataset, we selected county-level GDP observations for the time period of 2019-2024, removed aggregate geographic records, and standardized the data structure and measurements for the data. The cleaned dataset is available in our [GitHub repository.](https://github.com/sszatko2/Butter/blob/main/data/processed/bea_county_gdp_2019_2024.csv)

For the U.S. Census Bureau American Community Survey (ACS) dataset, we collected county-level housing and income estimates for the timeframe of 2019-2024, combined the separate annual datasets into one dataset, standardized county identifiers, and addressed the missing values within the data. We also calculated a home value to income ratio to support our analysis of housing affordability. The cleaned dataset is available in our [GitHub repository.](https://github.com/sszatko2/Butter/blob/main/data/processed/acs_county_housing_income_2019_2024.csv)

We also conducted ethical handling analysis for the three datasets by reviewing the official data use policies of the Bureau of Labor Statistics, Bureau of Economic Analysis, and U.S. Census Bureau American Community Survey. This review helped us to identify the relevant considerations for privacy and confidentiality, copyright restrictions, proper source attribution, and responsible data modification and redistribution when handling the data for our project. To document our compliance with each of the sources’ policies, we created a Data Sources and Attribution section in our GitHub repository’s README.md file, including the required API disclaimer for the U.S. Census Bureau and acknowledgements of the original data sources.  

We also completed an initial draft of the Data Profile section for our final project report where we examined each dataset’s structure, variables, geographic and temporal coverage, data quality characteristics, and their relevance to our project’s research questions on housing affordability in the United States. We also reviewed each agency’s official data-use policies to identify any ethical and legal considerations for our project regarding privacy, copyright, attribution, and restrictions on data redistribution. We also  confirmed that the three datasets contained complementary county-level information for integration. We also identified challenges involving differences in geographic coverage, missing observations, and reporting methodologies between the datasets that will have to be addressed for integration. 

## Updated Project Timeline

### Week 14 (Fall Break)

1. **Task 1: Pre-integration Data Quality Assessment:** We will assess the data quality of our chosen datasets across the dimensions of accuracy, completeness, timeliness, and consistency.
   - **Team Member:** Brennan Ryan

2. **Task 2: Data Cleaning:** We will clean the data prior to integration.
   - **Team Member:** Madelyn McNamara

3. **Task 3: Write Data Cleaning Section of Final Report:** We will document our pre-integration data quality assessment results and data cleaning in the final report.
    - **Team Member:** Aidan Flaherty

4. **Task 4: Data Integration:** We will integrate our datasets.
    - **Team Member:** Samantha Szatko

5. **Task 5: Post-Integration Data Quality Assessment:** We will assess the quality of the integrated data across the dimensions of accuracy, completeness, timeliness, and consistency.
    - **Team Member:** Brennan Ryan

6. **Task 6: Write Data Quality Section of Final Report:** We will document results of data quality assessment in the final report and explain how our assessment provides evidence that integration is reasonably successful.
    - **Team Member:** Aidan Flaherty

7. **Task 7: Complete and Submit Interim Status Report:** We will report the status of our project and submit the `StatusReport.md` through GitHub.
    - **Team Member:** Madelyn McNamara

8. **Task 8: Workflow Automation and Provenance:** We will create a workflow containing every operation we performed for reproducing our cleaned data which will be included in the final report.
    - **Team Member:** Samantha Szatko

### Week 15

9. **Task 9: Complete Data Analysis:** We will conduct analysis of our cleaned and integrated data to answer our research questions.
    - **Team Member:** Brennan Ryan

10. **Task 10: Visualize Data for Final Report:** We will generate visualizations to assist with data analysis for the final report.
    - **Team Member:** Madelyn McNamara

11. **Task 11: Write Findings and Future Work Sections of Final Report:** We will document the results of our analysis and document the steps used to analyze and visualize data as well as write a brief discussion of any lessons learned for potential future work.
    - **Team Member:** Aidan Flaherty

12. **Task 12: Write Challenges Section of Final Report:** We will discuss the main challenges encountered while working on the project.
    - **Team Member:** Samantha Szatko

13. **Task 13: Write Reproduction Steps for Final Report:** We will document the sequence of steps required for our results to be reproduced.
    - **Team Member:** Brennan Ryan

14. **Task 14: Metadata and Data Documentation:** We will make sure that all necessary metadata is included and that data and references used is properly documented.
    - **Team Member:** Madelyn McNamara

15. **Task 15: Write Summary Section for Final Report:** We will write the summary section for the final report including a description of our project, motivation, research questions, and brief overview of the findings from our analysis.
    - **Team Member:** Aidan Flaherty

16. **Task 16: Refine Final Report:** We will go through our report to refine the language and make sure that it covers all required elements.
    - **Team Member:** Samantha Szatko

17. **Task 17: Submit Final Report:** We will submit the final report according to the submission guidelines outlined in the Course Project Instructions document.
    - **Team Member:** Brennan Ryan

## Challenges

One of the challenges we encountered involved differences in geographic coverage and data availability across our three datasets. For example, there were missing GDP observations associated with changes in county geographic boundaries in both Connecticut and Alaska. We also found that the three datasets contain a different amount of county observations per year, which could create unmatched datasets during integration. Another issue we found was that the U.S. Census Bureau American Community Survey (ACS) dataset uses five-year estimates while the Bureau of Labor Statistics (BLS) and Bureau of Economic Analysis (BEA) datasets provide annual statistics which limit data comparison across different years for the three datasets. To address these challenges, we standardized geographic identifiers, kept the identified missing values in favor of replacing them with potentially misleading estimates, and documented the differences in reporting methodologies between the three datasets. However, these issues will require further attention when we begin the integration process.

## Individual Summaries

### Samantha Szatko

I downloaded and processed the Bureau of Labor Statistics (BLS), Local Area Unemployment Statistics (LAUS), Bureau of Economic Analysis (BEA) County GDP, and U.S. Census Bureau American Community Survey (ACS) datasets. I cleaned and organized the raw data into CSV format for each dataset and uploaded the processed files into our GitHub repository. I also conducted analysis for ethical data handling by reviewing each sources’ data-use policies and identified relevant considerations related to privacy, copyright, attribution, and data redistribution, all of which will be addressed in our project’s final report. I also drafted the Data Profile section for the final report. 




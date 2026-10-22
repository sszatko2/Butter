
# Housing Affordability in the United States

## Overview

**Goal of Project:** Housing costs vary greatly throughout the United States and it is not always clear what factors play a role in this. In this project we will examine what roles factors like unemployment and economic output have when it comes to association with housing affordability.

**Planned Approach:** Our project will follow the USGS Science Data Lifecycle Model. We will begin by planning the datasets we will use and the strategy we will employ to organize the data, then acquire the datasets, process the data through reproducible cleaning and integration, and finally analyze the data to answer our research questions and document our process and analysis results in a final report.

## Team

**Member Roles:**

1. **Data Acquisition and Organization Lead**
   - **Team Member:** Brennan Ryan
   - Responsible for finding and downloading the datasets needed for the project. Makes sure the data comes from reliable sources and is organized so the rest of the team can easily work with it.

2. **Data Quality and Cleaning Lead**
   - **Team Member:** Madelyn McNamara
   - Responsible for checking the datasets for missing information, errors, and inconsistencies. Works on cleaning up these issues so the data is accurate and ready to be combined.

3. **Data Integration and Workflow Lead**
   - **Team Member:** Aidan Flaherty
   - Responsible for combining the three datasets using shared information, such as county codes. Also works on creating a workflow that allows the data processing steps to be repeated.

4. **Data Analysis and Documentation Lead**
   - **Team Member:** Samantha Szatko
   - Responsible for analyzing the combined data to answer our research questions and creating graphs to show the results. Also helps organize and write the final report to explain our findings and the work completed.

## Research or Business Question(s)

**Housing Affordability in the United States**

- Which counties have the highest home prices compared with household income?
- Are counties with higher unemployment rates less affordable?
- Which states have the largest differences in housing affordability?
- How does a county's economic output relate to its housing affordability?

## Datasets

1. **United States Census Bureau County Housing Prices (2020-2024)**
   - **Link:** https://api.census.gov/data/2024/acs/acs5?get=NAME%2CB19013_001E%2CB25077_001E%2CB25064_001E&for=county%3A%2A&in=state%3A%2A&key=YOUR_API_KEY
   - You'll need to request an API key through email and replace the `YOUR_API_KEY` section of the link with it.

2. **Bureau of Labor Statistics (BLS), Local Area Unemployment Statistics (LAUS)**
   - **Description:** Annual average unemployment rate, labor force, and employment by county.
   - **Source:** https://www.bls.gov/lau/ (county data files)
   - **Contribution:** Local labor market conditions.
   - **Join Key:** State and county FIPS codes, plus year.

3. **Bureau of Economic Analysis (BEA) GDP by County**
   - **Link:** https://www.bea.gov/data/gdp/gdp-county-metro-and-other-areas
   - **Description:** Contains real and current-dollar GDP by county and year. Provides economic output and growth for the GDP questions.
   - **Join Key:** GeoFIPS (county FIPS code) plus year.

## Timeline

### Week 9

1. **Task 1: Data Lifecycle:** Decide the data lifecycle model that our workflow for the project will model within the overview of our project plan.
   - **Team Member:** Brennan Ryan

2. **Task 2: Identify Datasets:** We will evaluate three datasets that we will potentially use for the project.
   - **Team Member:** Madelyn McNamara

3. **Task 3: Submit Project Plan:** Finish writing and submit `ProjectPlan.md` through GitHub.
   - **Team Member:** Aidan Flaherty

### Week 10

4. **Task 4: Data and Organization:** We will decide on a specific storage and organization strategy for the data.
   - **Team Member:** Brennan Ryan

5. **Task 5: Data Collection and Acquisition:** We will acquire and download the data that we will use for the project.
   - **Team Member:** Madelyn McNamara

6. **Task 6: Ethical Data Handling:** We will identify and address any ethical or legal constraints associated with the data.
   - **Team Member:** Aidan Flaherty

7. **Task 7: Complete Data Profile Section of Report:** We will describe the structure, content, including our data and organization strategy and the ethical data handling identified earlier, and explain how the datasets relate to our questions.
   - **Team Member:** Samantha Szatko

### Week 11

8. **Task 8: Pre-integration Data Quality Assessment:** We will assess the data quality of our chosen datasets across the dimensions of accuracy, completeness, timeliness, and consistency.
   - **Team Member:** Brennan Ryan

9. **Task 9: Data Cleaning:** We will clean the data prior to integration.
   - **Team Member:** Madelyn McNamara

10. **Task 10: Write Data Cleaning Section of Final Report:** We will document our pre-integration data quality assessment results and data cleaning in the final report.
    - **Team Member:** Aidan Flaherty

11. **Task 11: Data Integration:** We will integrate our datasets.
    - **Team Member:** Samantha Szatko

### Week 12

12. **Task 12: Post-Integration Data Quality Assessment:** We will assess the quality of the integrated data across the dimensions of accuracy, completeness, timeliness, and consistency.
    - **Team Member:** Brennan Ryan

13. **Task 13: Write Data Quality Section of Final Report:** We will document results of data quality assessment in the final report and explain how our assessment provides evidence that integration is reasonably successful.
    - **Team Member:** Aidan Flaherty

14. **Task 14: Complete and Submit Interim Status Report:** We will report the status of our project and submit the `StatusReport.md` through GitHub.
    - **Team Member:** Madelyn McNamara

15. **Task 15: Workflow Automation and Provenance:** We will create a workflow containing every operation we performed for reproducing our cleaned data which will be included in the final report.
    - **Team Member:** Samantha Szatko

### Week 13

16. **Task 16: Complete Data Analysis:** We will conduct analysis of our cleaned and integrated data to answer our research questions.
    - **Team Member:** Brennan Ryan

17. **Task 17: Visualize Data for Final Report:** We will generate visualizations to assist with data analysis for the final report.
    - **Team Member:** Madelyn McNamara

18. **Task 18: Write Findings and Future Work Sections of Final Report:** We will document the results of our analysis and document the steps used to analyze and visualize data as well as write a brief discussion of any lessons learned for potential future work.
    - **Team Member:** Aidan Flaherty

19. **Task 19: Write Challenges Section of Final Report:** We will discuss the main challenges encountered while working on the project.
    - **Team Member:** Samantha Szatko

### Week 15

20. **Task 20: Write Reproduction Steps for Final Report:** We will document the sequence of steps required for our results to be reproduced.
    - **Team Member:** Brennan Ryan

21. **Task 21: Metadata and Data Documentation:** We will make sure that all necessary metadata is included and that data and references used is properly documented.
    - **Team Member:** Madelyn McNamara

22. **Task 22: Write Summary Section for Final Report:** We will write the summary section for the final report including a description of our project, motivation, research questions, and brief overview of the findings from our analysis.
    - **Team Member:** Aidan Flaherty

23. **Task 23: Refine Final Report:** We will go through our report to refine the language and make sure that it covers all required elements.
    - **Team Member:** Samantha Szatko

24. **Task 24: Submit Final Report:** We will submit the final report according to the submission guidelines outlined in the Course Project Instructions document.
    - **Team Member:** Brennan Ryan

## Constraints

- County boundaries and geographic classifications can change over time, which may make it difficult to match data between different sources.
- Some areas, such as independent cities, are treated as county equivalents, which may create differences in how locations are represented across datasets.
- Inflation can affect housing prices, income, and GDP differently, making comparisons across years more difficult.
- The Census ACS data uses five-year estimates, while the BLS and BEA provide annual data. This could make it difficult to compare information from the same time period.
- Just because two variables are related does not necessarily mean that one causes the other.

## Gaps

- We still need to determine which years will work best for comparing all three datasets.
- We need to confirm that all three datasets can be combined using county FIPS codes and determine how to handle any counties that do not match.
- We need to decide how we will measure housing affordability, such as comparing median home values to median household income.
- We still need to determine which cleaning methods will be necessary once we download and examine the datasets.

# **Istanbul Seaports Data - DSA210 Project**

## Project Overview

This project analyzes the daily passenger counts at Istanbul's seaports for the year 2024. Using datasets from the İBB Open Data Portal and supplementary weather data, the study explores seasonal variation, pier usage patterns, and how environmental factors such as wind affect ferry mobility.

The ultimate goal is to derive actionable insights for urban maritime transportation planning using statistical methods and data visualization.

## Objectives

- Examine daily and monthly variations in passenger numbers.
- Identify the busiest and least used seaports.
- Visualize passenger trends and detect behavioral patterns.
- Analyze the effect of weather variables (wind speed, humidity, temperature) on ferry usage.
- Investigate the difference in passenger counts between school terms and holiday periods.
- Conduct correlation and regression analysis to test statistical significance.
- Apply DSA210 course methods to real-world public transportation data.

## Motivation

Istanbul, being a densely populated metropolitan city with an extensive public transportation system, requires continuous data-driven evaluation. Understanding the factors that influence ferry usage, including seasonal changes and weather conditions, is essential for reliable urban transport planning.

Maritime transportation is particularly vulnerable to environmental factors like wind, which can disrupt service or change rider behavior. Additionally, school calendars (term vs. holiday periods) may influence commuter patterns, which are also explored in this study.

## Dataset

The primary dataset is downloaded from the [İBB Open Data Portal](https://ulasav.csb.gov.tr/dataset/34-istanbul-deniz-iskeleleri-yolcu-sayilari/resource/189d7304-2646-43f7-b4ba-3b689f444683) and includes:

- **Date**: Daily records for 2024
- **Station Name**: The seaport where the passengers boarded
- **Passenger Count**: Daily count per pier

### Additional Dataset: Weather and School Term Data

A supplementary weather dataset is downloaded from [WeatherSpark](https://tr.weatherspark.com) and includes:

- **Average Wind Speed (km/h)**
- **Maximum Wind Speed (km/h)**
- **Temperature (max, min)**
- **Humidity (%)**

Additionally, school calendar information is manually encoded as:

- **School Term (1)**: Dates when schools are open
- **Holiday Period (0)**: Dates when schools are on break

These variables are merged by date to conduct multivariate analysis.

## Tools and Technologies

- **Python**: Analysis and modeling
- **Pandas**: Data manipulation
- **Matplotlib & Seaborn**: Visualization
- **SciPy & Statsmodels**: Hypothesis testing and regression

## Analysis Plan

### Investigating the Impact of Weather and School Terms on Passenger Mobility

- **Data Preparation:**

  - Merge weather, school term, and passenger datasets by date.
  - Handle missing data and calculate average temperature.
  - Create categorical variables like wind condition (Calm, Breezy, Windy) and school term (Holiday vs School).

- **Visualizations:**

  - **Bar Plots:**
    - *Daily passenger count by day of the week and school term:* Shows how holidays impact weekday travel behavior.
    - *Daily passenger count by day of the week and wind condition:* Highlights the effect of wind on passenger numbers throughout the week.
  - **Heatmaps:**
    - *Correlation matrix:* Shows relationships between daily passenger count and weather variables (wind, humidity, temperature), as well as school term.
  - **Boxplots:**
    - *Holiday vs School Term:* Compares passenger distribution clearly, showing higher counts during holidays.
  - **Multivariate Bar Plot (Triple Grouping):**
    - *Passenger count grouped by weekday and wind category (Calm, Breezy, Windy):* Reveals compound patterns influenced by both time and weather.

- **Hypothesis Testing:**

  **1. Weather Effect**

  - Null Hypothesis (H₀): Weather variables have no significant effect on passenger numbers.

  - Alternative Hypothesis (H₁): At least one weather variable has a significant effect on passenger numbers.

  - ANOVA results:

    - Wind Speed: p-value < 0.0001 (**significant**)
    - Humidity: p-value = 0.48 (not significant)
    - Temperature: p-value = 0.95 (not significant)

  ✅ H₀ is rejected.

  **Conclusion:** Wind speed significantly affects ferry usage, while humidity and temperature do not.

  **2. School Term Effect**

  - Null Hypothesis (H₀): There is no significant difference in the average number of daily ferry passengers between school holiday periods and school term periods.

  - Alternative Hypothesis (H₁): The average number of daily ferry passengers during school holidays is significantly higher than during school term periods.

  - p-value = 0.0021 (**significant**)

  ✅ H₀ is rejected.

  **Conclusion:** Daily ferry usage is significantly higher during holiday periods compared to school terms.

- **Regression Analysis:**

  - A multiple linear regression model was applied.
  - Wind speed and school term emerged as significant predictors of daily passenger count.
  - The model confirms findings from correlation and hypothesis tests.

## Findings

- Daily passenger usage is higher during holiday periods than school terms.
- Windy days correspond to a lower number of ferry passengers.
- Weekday and weather combinations (e.g., Windy Fridays) show clear impact patterns.
- Temperature and humidity alone do not explain changes in ferry usage.

## Limitations and Future Work

- The analysis is limited to 2024 and does not consider long-term trends.
- Including more years would allow more robust seasonal modeling.
- Future versions could integrate tourism data, service disruption logs, and ticket pricing.

## Conclusion

This project provides actionable insights on how Istanbul's maritime transport system is influenced by external factors like wind and school calendars. The findings can support public service planning, schedule optimization, and seasonal resource allocation. By applying DSA210 course methods, the project bridges academic knowledge with real-world transportation data challenges.


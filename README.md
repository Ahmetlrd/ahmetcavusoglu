# **Istanbul Seaports Data - DSA210 Project**

## **Project Overview**

This project aims to analyze the number of passengers at Istanbul's seaports throughout 2024. Using data from the İBB Open Data Portal, various analyses will be conducted on seasonal variations, the most frequently used piers, and passenger mobility.

The goal of this study is to gain data-driven insights into Istanbul's maritime transportation usage and generate conclusions for urban transportation planning.

## **Objectives**

- Analyze the monthly distribution of passenger numbers at Istanbul's seaports to observe spring-summer-fall-winter differences.
- Identify the most and least frequently used piers.
- Visualize passenger mobility to detect trends.
- Investigate the impact of wind speed on passenger numbers.
- Provide data-driven recommendations for transportation optimization.
- Apply the concepts from my DSA 210 course to real-world scenarios, deepening my understanding of data analysis and visualization.

## **Motivation**

This project was chosen to understand the usage patterns of maritime transportation in Istanbul and to apply data science techniques to a real-world problem. In a particular metropolitan city like Istanbul, public transportation analyses play a crucial role in transportation planning and infrastructure development.

Additionally, external factors such as weather conditions may significantly influence passenger mobility. Therefore, wind speed data will be incorporated into the analysis to examine its potential effect on maritime transportation.

## **Dataset**

The dataset used in this project is obtained from the [İBB Open Data Portal](https://ulasav.csb.gov.tr/dataset/34-istanbul-deniz-iskeleleri-yolcu-sayilari/resource/189d7304-2646-43f7-b4ba-3b689f444683) by downloading and contains passenger counts at Istanbul's seaports for the year 2024. The dataset includes the following columns:

- **Year**: Data from 2024
- **Month**: Covers the period from January to December
- **Authority Name**: The entity managing the ferry service
- **Station Name**: The seaports where passenger transportation occurs
- **Passenger Count**: The total number of passengers passing through a specific pier in a given month

### **Additional Dataset: Wind Speed Data**

An additional dataset from [WeatherSpark](https://tr.weatherspark.com/y/95434/%C4%B0stanbul-T%C3%BCrkiye-Ortalama-Hava-Durumu-Y%C4%B1l-Boyunca#Figures-WindSpeed) will be used to analyze the impact of wind speed on passenger mobility by downloading. The dataset includes:

- **Date**: The day of recorded wind speed.
- **Average Wind Speed (km/h)**: The daily mean wind speed in Istanbul.
- **Max Wind Speed (km/h)**: The highest recorded wind speed of the day.

## **Tools and Technologies**

The following tools will be used for data analysis and visualization:

- **Python**: Data processing and analysis
- **Pandas**: Dataframe manipulation
- **Matplotlib and Seaborn**: Data visualization
- **SciPy**: Statistical analysis and hypothesis testing
- **Folium or Geopandas**: Mapping seaports in Istanbul (optional)

## **Analysis Plan**

### **Investigating the Impact of Wind Speed on Passenger Mobility**

To explore how wind speed affects passenger counts, correlation analysis, regression models, and time series plots will be utilized.

- **Data Collection:**
  - The wind speed dataset will be merged with the passenger dataset based on the corresponding dates.
  - Missing values will be handled, and the units will be standardized.

- **Visualization:**
  - Scatter plots will be created to examine the relationship between wind speed and passenger numbers.
  - A heatmap will be used to show correlations between wind speed and other variables.
  - Time series plots will compare passenger trends with wind speed fluctuations over the months.

- **Hypothesis Testing:**

  Null Hypothesis (H₀): Wind speed has no significant effect on passenger numbers.

  Alternative Hypothesis (H₁): Wind speed has a significant effect on passenger numbers.

- **Statistical Analysis:**
  - A linear regression model will be applied to determine if there is a measurable impact of wind speed on ferry passenger numbers.
  - Multiple regression may be used to control for other seasonal effects.

## **Findings**

The following insights are expected as a result of these analyses:

- Seasonal differences in maritime transportation usage will be clearly observed.
- Identifying the busiest piers can help optimize transportation planning.
- The impact of particular months on passenger numbers will be revealed.
- The influence of wind speed on passenger mobility will be analyzed, potentially uncovering insights for service adjustments during high-wind periods.

## **Limitations and Future Work**

- **Limitations:** Since the dataset covers only 2024, it will not be possible to analyze long-term trends.
- **Future Studies:** By incorporating data from multiple years, long-term trends in Istanbul’s sea transportation can be analyzed.
- **Additional Data Usage:** External factors such as weather conditions, service disruptions, and tourism activity can be included to perform a more comprehensive analysis.

## **Conclusion**

This project aims to understand the usage patterns of maritime transportation in Istanbul and apply data science techniques to a real-world problem. By considering seasonal changes, pier-based analysis, and weather conditions, passenger mobility will be examined in detail.

The findings of this study may contribute to more efficient decision-making in maritime transportation management and urban planning. At the end of the project, data-driven optimization recommendations for Istanbul’s maritime transportation system will be provided.


# **Number of Passengers at Istanbul Seaports-DSA210Project**

## **Project Overview**

This project aims to analyze the number of passengers at Istanbul's ferry piers throughout 2024. Using data from the İBB Open Data Portal, various analyses will be conducted on seasonal variations, the most frequently used piers, and passenger mobility.

The goal of this study is to gain data-driven insights into Istanbul's maritime transportation usage and generate conclusions for urban transportation planning.

## **Objectives**

- Analyze the monthly distribution of passenger numbers at Istanbul's ferry piers to observe spring-summer-fall-winter differences.
- Identify the most and least frequently used piers.
- Visualize passenger mobility to detect trends.
- Provide data-driven recommendations for transportation optimization.
- Apply Sata Science Skills\:Apply the concepts from my DSA 210 course to real-world scenarios, deepening my understanding of data analysis and visualization.

## **Motivation**

This project was chosen to understand the usage patterns of maritime transportation in Istanbul and to apply data science techniques to a real-world problem. In a particular metropolitan city like Istanbul, public transportation analyses play a crucial role in transportation planning and infrastructure development.

## **Dataset**

The dataset used in this project is obtained from the İBB Open Data Portal and contains passenger counts at Istanbul's Seaports for the year 2024. The dataset includes the following columns:

- **Year**: Data from 2024
- **Month**: Covers the period from January to December
- **Authority Name**: The entity managing the ferry service
- **Station Name**: The seaports where passenger transportation occurs
- **Passenger Count**: The total number of passengers passing through a specific pier in a given month

Since the dataset contains separate records for each month, it allows for time series analysis.

## **Tools and Technologies**

The following tools will be used for data analysis and visualization:

- **Python**: Data processing and analysis
- **Pandas**: Dataframe manipulation
- **Matplotlib and Seaborn**: Data visualization
- **SciPy**: Statistical analysis and hypothesis testing
- Folium or Geopandas: Mapping ferry piers in Istanbul (maybe)

## **Analysis Plan**

### **1. Monthly Passenger Distribution and Seasonal Differences**

To examine changes in passenger numbers between summer and winter months, boxplots and time series plots will be used.

- **Hypothesis Testing:**

  Null Hypothesis (H₀): There is no significant difference in passenger numbers between summer (June, July, August) and winter months.

  Alternative Hypothesis (H₁): Passenger numbers in summer (June, July, August) are significantly higher than in winter months.
- ***Statistical Test:*** ANOVA or t-test will be applied to determine if the seasonal differences are statistically significant.
- **Visualization:** A time series graph of monthly passenger counts will be created, and moving averages will be calculated for trend analysis.

### **2. Identifying the Most and Least Used Piers**

To determine which piers are the busiest and least used, bar charts and heatmaps will be utilized.

- **Hypothesis Testing:**

  Null Hypothesis (H₀): There is no significant difference in ferry traffic between central locations along the Bosphorus (Beşiktaş, Kadıköy, Eminönü, etc.) and other ferry piers.

  Alternative Hypothesis (H₁): Central locations along the Bosphorus (Beşiktaş, Kadıköy, Eminönü, etc.) have significantly higher ferry traffic than other ferry piers.
- **Analysis:** Total passenger numbers for each pier will be calculated, and the top and bottom piers will be listed.
- **Visualization:** A map of the piers will be created, highlighting the busiest locations using a heatmap.

Additional data sources (For example: meteorological data and official holiday information) may be used for this analysis.

## **Findings**

The following insights are expected as a result of these analyses:

- Seasonal differences in maritime transportation usage will be clearly observed.
- Identifying the busiest piers can help optimize transportation planning.
- The impact of particular months on passenger numbers will be revealed.

## **Limitations and Future Work**

- **Limitations:** Since the dataset covers only 2024, it will not be possible to analyze long-term trends.
- **Future Studies:** By incorporating data from multiple years, long-term trends in Istanbul’s sea transportation can be analyzed.
- **Additional Data Usage:** External factors such as weather conditions, service disruptions, and tourism activity can be included to perform a more comprehensive analysis.

## **Conclusion**

This project aims to understand the usage patterns of maritime transportation in Istanbul and apply data science techniques to a real-world problem. By considering seasonal changes, pier-based analysis, and various external factors, passenger mobility will be examined in detail.

The findings of this study may contribute to more efficient decision-making in maritime transportation management and urban planning. At the end of the project, data-driven optimization recommendations for Istanbul’s maritime transportation system will be provided.


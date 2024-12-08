# Automated Data Analysis Report for Happiness

## Dataset: happiness.csv

### Dataset Overview
- **Columns**: ['Country name', 'year', 'Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect', 'Negative affect']
- **Missing Values**: {'Country name': 0, 'year': 0, 'Life Ladder': 0, 'Log GDP per capita': 28, 'Social support': 13, 'Healthy life expectancy at birth': 63, 'Freedom to make life choices': 36, 'Generosity': 81, 'Perceptions of corruption': 125, 'Positive affect': 24, 'Negative affect': 16}

### Key Insights
# Dataset Analysis Summary

## Key Insights
1. **Data Completeness**: Most columns contain missing values; the 'Generosity' and 'Perceptions of corruption' columns have the highest number of missing entries (81 and 125, respectively), indicating significant gaps that could impact analyses.
2. **Country Distribution**: The dataset includes 165 unique countries, with Argentina being the most frequently represented, occurring 18 times. This may suggest a regional focus or completeness issues for certain countries.
3. **Life Ladder Score**: The average “Life Ladder” score is approximately 5.48, with a range from 1.281 to 8.019, indicating varying levels of subjective well-being across different countries.
4. **GDP Influence**: The average “Log GDP per capita” is around 9.40, reflecting differences in economic prosperity. This metric shows a potential correlation with the Life Ladder score given the economic dimensions of happiness.
5. **Health Indicators**: The average healthy life expectancy at birth is 63.40 years, with significant deviations marked by standard deviation (6.84), suggesting disparities in health outcomes on a global scale.
6. **Social Support**: Social support averages 0.809, indicating a generally high sense of community or support in many regions.
7. **Freedom Index**: With an average score of 0.75 for “Freedom to make life choices,” it suggests that many individuals feel they have some level of autonomy in their lives, although there is still room for improvement.

## Dataset Overview
The dataset contains 2,363 rows and 11 columns, representing various socio-economic indicators and subjective dimensions of well-being for different countries over several years. The columns help detail the connections between GDP, social support, health, individual freedoms, perceptions of corruption, and personal happiness.

## Key Findings
1. **Correlation Exploration**: Initial observations suggest that higher GDP per capita and social support are correlated with higher life ladder scores, indicative of greater satisfaction and happiness.
2. **Impact of Missing Data**: The significant amount of missing data in key indicators, particularly 'Generosity' and 'Perceptions of corruption', limits the explorability of relationships in comprehensive analyses and might skew results if not handled properly.
3. **Temporal Aspects**: The dataset spans from 2005 to 2023, showing progression of happiness and economic indicators over time, which can be vital for studying trends and changes in societal perspectives.
4. **Mental Health Correlates**: The Positive and Negative Affects suggest that while the average Positive Affect score is above 0.65, Negative Affect hovers around 0.27, indicating a somewhat balanced psychological state, though more examination is needed in specific demographics or regions.

## Recommendations
1. **Address Missing Data**: Use imputation techniques or consider different methods of analysis that can accommodate missing values to provide a more complete view of the data.
2. **Deepen Analysis**: Conduct more detailed correlation analysis between Life Ladder and economic variables like Log GDP, healthcare access, and social support to better understand contributing factors to happiness.
3. **Regional Focus Studies**: Given the concentration of countries like Argentina in the dataset, it may be beneficial to conduct regional studies to see how cultural differences affect perceptions of happiness and well-being.
4. **Longitudinal Studies**: Implement longitudinal analysis to understand trends and changes in the indicators over time, which could provide insights on the effects of global events on well-being and economic conditions.

## Conclusion
The dataset presents a valuable resource for understanding the interplay between economic indicators, social support, healthcare, individual freedoms, and subjective well-being across nations. However, significant missing data must be addressed to ensure robust analyses and insights. Continuing this research will be crucial in addressing global disparities in happiness and well-being, ultimately aiding policymakers in nation-building and development strategies.

### Outlier Detection Results
Detected outliers in 'year': 0 rows
Detected outliers in 'Life Ladder': 2 rows
Detected outliers in 'Log GDP per capita': 1 rows
Detected outliers in 'Social support': 48 rows
Detected outliers in 'Healthy life expectancy at birth': 20 rows
Detected outliers in 'Freedom to make life choices': 16 rows
Detected outliers in 'Generosity': 39 rows
Detected outliers in 'Perceptions of corruption': 194 rows
Detected outliers in 'Positive affect': 9 rows
Detected outliers in 'Negative affect': 31 rows

### Feature Importance Analysis
|    | Feature                          |   Importance |
|---:|:---------------------------------|-------------:|
|  3 | Social support                   |    0.271567  |
|  4 | Healthy life expectancy at birth |    0.107955  |
|  2 | Log GDP per capita               |    0.10545   |
|  0 | year                             |    0.104128  |
|  8 | Positive affect                  |    0.103454  |
|  7 | Perceptions of corruption        |    0.0897795 |
|  5 | Freedom to make life choices     |    0.0747241 |
|  1 | Life Ladder                      |    0.0741952 |
|  6 | Generosity                       |    0.0687488 |

### Correlation Analysis
Correlation Matrix saved as C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness\correlation_matrix.png

### Visualizations
![Correlation Heatmap](C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/correlation_heatmap.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/year_histogram.png](year_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Life Ladder_histogram.png](Life Ladder_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Log GDP per capita_histogram.png](Log GDP per capita_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Social support_histogram.png](Social support_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Healthy life expectancy at birth_histogram.png](Healthy life expectancy at birth_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Freedom to make life choices_histogram.png](Freedom to make life choices_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Generosity_histogram.png](Generosity_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Perceptions of corruption_histogram.png](Perceptions of corruption_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Positive affect_histogram.png](Positive affect_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\happiness/Negative affect_histogram.png](Negative affect_histogram.png)

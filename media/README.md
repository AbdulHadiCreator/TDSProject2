# Automated Data Analysis Report for Media

## Dataset: media.csv

### Dataset Overview
- **Columns**: ['date', 'language', 'type', 'title', 'by', 'overall', 'quality', 'repeatability']
- **Missing Values**: {'date': 99, 'language': 0, 'type': 0, 'title': 0, 'by': 262, 'overall': 0, 'quality': 0, 'repeatability': 0}

### Key Insights

1. **Missing Values**: The dataset contains a significant number of missing values, particularly in the 'date' (99 missing) and 'by' (262 missing) columns. Addressing these is crucial for further analysis.

2. **Language and Type Distribution**: The dataset predominantly focuses on English language entries (1306 out of 2652) and movies (2211 out of 2652), indicating a potential bias towards popular media.

3. **Overall Ratings**: The average overall rating is approximately 3.05, indicating a generally satisfactory reception among the entries. However, it has a standard deviation of 0.76, which suggests variability in how different entries are rated.

4. **Quality Ratings**: The average quality rating is slightly higher at about 3.21, indicating that movies may often be perceived as more qualitative than their overall rating.

5. **Repeatability**: The mean repeatability scoring is lower (1.49), suggesting that many entries lack consistency or may not be easily re-watched or appreciated multiple times.

### Dataset Overview

- **Columns**: The dataset consists of 8 columns focused on media attributes like 'date', 'language', 'type', and various ratings (overall, quality, repeatability).
- **Size**: It contains 2652 total records, highlighting a robust dataset, but attention is needed on the missing values.
- **Unique Values**: The titles, contributors, and entry dates are diverse, with 2312 unique titles and 1528 unique contributors.

### Key Findings

1. **Outlier Analysis**: Significant outliers were detected in the 'overall' ratings (1216 rows) and fewer in 'quality' (24 rows). This indicates that while most entries are rated around the average score, many have extremely high or low ratings that could skew the interpretation of the data.

2. **Feature Importance**: The analysis indicates that 'overall' is the most significant predictor of satisfaction/ratings, with a very high importance score (82.17%) compared to 'quality' (17.83%).

3. **Cluster Analysis**: K-Means clustering successfully identified 3 distinct clusters in terms of overall, quality, and repeatability scores. Patterns in these clusters can inform audience targeting and content strategy.

### Recommendations

1. **Data Cleaning**: Missing data should be addressed through imputation or careful removal. Furthermore, further investigation of the outliers in the 'overall' scores is recommended to either understand the reasons behind extreme ratings or to consider removing them from aggregated analyses.

2. **Focus on High-Quality Content**: Given the cluster analysis, accommodations should focus on high-quality titles (as indicated by high ratings) to retain audience engagement. Consider investing in similar genres or thematic content found within the clusters.

3. **Explore Contributor Patterns**: Investigate commonalities related to high-rated titles by different contributors ('by'). It may be beneficial to create partnerships or highlight contributors that consistently deliver high ratings.

4. **Enhance Repeatability**: Strategies should be employed to enhance repeatability aspects of the content, possibly by promoting fan-favorite titles more aggressively or through secondary content that enhances viewers' experiences.

### Conclusions

The dataset offers a solid foundation for understanding audience preferences in media ratings, especially regarding 'overall' satisfaction and 'quality.' Key outliers should be addressed to ensure data integrity, and focused strategies should target identified patterns through clustering to foster engagement and improve the quality of media entries. By acting on these insights, the dataset can provide more pronounced strategic advantages in content curation and audience engagement.

### Outlier Detection Results
Detected outliers in 'overall': 1216 rows
Detected outliers in 'quality': 24 rows
Detected outliers in 'repeatability': 0 rows

### Feature Importance Analysis
|    | Feature   |   Importance |
|---:|:----------|-------------:|
|  0 | overall   |     0.821653 |
|  1 | quality   |     0.178347 |

### Correlation Analysis
Correlation Matrix saved as C:\Users\Abdul Hadi\Desktop\TdsProject2\media\correlation_matrix.png

### Clustering Analysis
K-Means clustering successfully performed with 3 clusters on numeric columns: ['overall', 'quality', 'repeatability']. Results plotted in two dimensions.

### Distribution Analysis
Boxplot created for overall.
Boxplot created for quality.
Boxplot created for repeatability.

### Visualizations
![Correlation Heatmap](C:\Users\Abdul Hadi\Desktop\TdsProject2\media/correlation_heatmap.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\media/overall_histogram.png](overall_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\media/quality_histogram.png](quality_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\media/repeatability_histogram.png](repeatability_histogram.png)

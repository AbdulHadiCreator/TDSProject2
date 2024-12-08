# Automated Data Analysis Report for Media

## Dataset: media.csv

### Basic Analysis
- Columns: ['date', 'language', 'type', 'title', 'by', 'overall', 'quality', 'repeatability']
- Missing Values: {'date': 99, 'language': 0, 'type': 0, 'title': 0, 'by': 262, 'overall': 0, 'quality': 0, 'repeatability': 0}

### Key Insights
### Dataset Analysis Summary: Insights and Recommendations

The dataset provides insights into a collection of media reviews characterized by several attributes: publication date, language, type of media, title, author, and three quantitative measures of assessment: overall rating, quality, and repeatability. 

#### **Key Findings:**

1. **Missing Values:**
   - The dataset contains missing values in the 'date' (99 entries) and 'by' (262 entries) columns. This suggests a potential issue with data completeness concerning when the reviews were published and who authored them, which could limit our analysis of trends over time or the influence of specific authors.
  
2. **Language and Media Type Distribution:**
   - The reviews are primarily in **English**, which constitutes over half of the entries (1306 out of 2652). 
   - The dataset predominantly features **movies** (2211 entries), indicating a rich focus on cinematic evaluations.
   - With 11 unique languages captured, there’s an opportunity for expanding insights into non-English media.

3. **Title and Author Diversity:**
   - There are 2312 unique titles, with the most common title, "Kanda Naal Mudhal," appearing 9 times. 
   - The author field demonstrates significant diversity, featuring 1528 unique authors. The most frequent contributor—Kiefer Sutherland—presents opportunities for targeted analysis of his reviews.

4. **Assessment Metrics:**
   - The **overall rating** averages approximately **3.05** (on a scale of 1 to 5), with a standard deviation of **0.76**, suggesting a moderate favorable reception across the dataset.
   - The **quality rating** averages slightly higher at **3.21**, indicating that although the media may be well-enjoyed overall, perceptions of production quality are slightly better.
   - The **repeatability score**, averaging **1.49**, suggests that while users might enjoy the content, they may not find it compelling enough for repeated viewing.

5. **Statistical Trends:**
   - The majority of the ratings tend towards the middle of their respective scales, with both the overall and quality rating medians at 3. This centrism highlights the potential for polarization in viewer opinions—further investigation could illuminate which factors correlate with higher or lower ratings.

#### **Visualizations:**
- **Correlation Heatmap:** This visualization likely demonstrates the relationships between the quantitative assessments (overall, quality, repeatability), which could indicate areas where enhancement or adjustment in production quality may improve overall viewer satisfaction.
  
- **Histograms of Numeric Columns:** These distributions will provide insights into tendencies and biases in ratings, such as whether there are clusters at higher or lower ratings which warrant further investigation.

#### **Recommendations:**

1. **Data Cleaning:**
   - Address missing values by investigating the possibility of imputing or reconstructing 'date' and 'by' fields where feasible. This will strengthen the integrity of analyses performed on the dataset.

2. **Author and Content Analysis:**
   - Conduct deeper analysis on frequently referenced authors and titles. Understanding the nature of these evaluations can reveal insights into common themes or notable styles that appeal to audiences.

3. **Focus on User Engagement:**
   - Explore content properties that lead to higher quality and overall ratings. Knowing what drives viewer satisfaction could inform future media production strategies.

4. **Diversity Expansion:**
   - Given the substantial number of reviews in English, consider strategies for expanding review accessibility into other languages, which can attract a more diverse audience.

5. **Sentiment Analysis:**
   - Implement advanced text analysis methods to gauge sentiment in the reviews' narratives, linking qualitative assessments with quantitative scores for richer insights.

By following these recommendations, we can enhance our understanding of consumer preferences and improve the overall quality and selection of future media products based on viewer feedback.

### Visualizations
![Correlation Heatmap](correlation_heatmap.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\media/overall_histogram.png](overall_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\media/quality_histogram.png](quality_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\media/repeatability_histogram.png](repeatability_histogram.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Automated Data Analysis Report for Happiness

## Dataset: happiness.csv

### Basic Analysis
- Columns: ['Country name', 'year', 'Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect', 'Negative affect']
- Missing Values: {'Country name': 0, 'year': 0, 'Life Ladder': 0, 'Log GDP per capita': 28, 'Social support': 13, 'Healthy life expectancy at birth': 63, 'Freedom to make life choices': 36, 'Generosity': 81, 'Perceptions of corruption': 125, 'Positive affect': 24, 'Negative affect': 16}

### Key Insights
### Dataset Analysis Summary: Insights and Recommendations

#### Overview
The dataset comprises information on various well-being indicators across different countries from 2005 to 2023. Key variables include measures of life satisfaction (Life Ladder), social support, economic indicators (Log GDP per capita), and perceptions of well-being such as positive and negative affect levels. 

#### Insights

1. **Life Ladder and GDP Correlation**: 
   - The mean Life Ladder score is approximately 5.48 with a standard deviation of 1.12, indicating a general sense of well-being among the surveyed population. 
   - The correlation between 'Log GDP per capita' and 'Life Ladder' likely indicates a positive relationship; wealthier nations tend to report higher life satisfaction. This underscores the economic aspect of happiness, suggesting policies aimed at economic growth could elevate national well-being.

2. **Social Support and Life Satisfaction**: 
   - With a mean social support score of 0.81 and ranges suggesting it is a robust contributor to life satisfaction, this suggests that countries with higher social support reporting are likely to correlate with higher Life Ladder scores.
   - This data emphasizes the necessity of community and social networks in enhancing citizens' life satisfaction, suggesting that initiatives to foster social connectivity (through community programs) could improve overall happiness.

3. **Expectations of Freedom**: 
   - The mean for 'Freedom to make life choices' is assessed at 0.75, revealing that personal autonomy is highly valued. Countries providing greater freedoms likely see improvements in citizen happiness.
   - This finding advocates for continuous support of individual freedoms and rights as essential components of societal well-being.

4. **Generosity and Corruption Perceptions**: 
   - The low mean score of Generosity (0.0000977) alongside the high mean for Perceptions of corruption (0.74) raises eyebrows. This suggests that a culture of generosity may be underdeveloped in contexts where corruption is perceived as high.
   - There is a potential for policy-oriented programs targeting community engagement and transparency which may foster a more generous disposition alongside civic trust.

5. **Mental Well-being**: 
   - The measured Positive affect average (0.65) compared to Negative affect (0.27) indicates a generally favorable emotional landscape among participants.
   - Programs focused on mental health awareness and reducing stigma can further buoy this aspect of well-being. Mental health initiatives could provide supportive environments that prioritize emotional well-being, combating negative affect levels.

#### Recommendations

1. **Economic and Social Policy Integration**: Focus on harmonizing economic initiatives with social support enhancement. Policies encouraging economic growth should include social programs aimed at improving community connections and well-being.

2. **Community Engagement Initiatives**: Create and fund programs to increase social interaction among citizens to bolster social support scores. Initiatives could include local events, forums, or online community-building activities.

3. **Promote Autonomy**: Safeguard and promote individual freedoms through legislative frameworks that empower citizens, ensuring that they feel they have a significant input into their lives.

4. **Address Corruption Issues**: Advocate for transparency and accountability within governments and institutions to nurture public trust and potentially improve both variables of generosity and life satisfaction.

5. **Mental Health Programs**: Invest in comprehensive mental health education and resources to cultivate a culture that values emotional well-being, increases awareness, and reduces the stigma surrounding mental health.

By addressing these interconnected areas—economic growth, social support, personal freedom, transparency, and mental health—we can work towards creating a more satisfied, connected, and overall happier global community. The data signals that while there is a good foundation, there’s ample opportunity for growth and improvement in societal well-being.

### Visualizations
![Correlation Heatmap](correlation_heatmap.png)
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

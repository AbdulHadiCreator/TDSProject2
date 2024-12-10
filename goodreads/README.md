# Automated Data Analysis Report for Goodreads

## Dataset: goodreads.csv

### Dataset Overview
- **Columns**: ['book_id', 'goodreads_book_id', 'best_book_id', 'work_id', 'books_count', 'isbn', 'isbn13', 'authors', 'original_publication_year', 'original_title', 'title', 'language_code', 'average_rating', 'ratings_count', 'work_ratings_count', 'work_text_reviews_count', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5', 'image_url', 'small_image_url']
- **Missing Values**: {'book_id': 0, 'goodreads_book_id': 0, 'best_book_id': 0, 'work_id': 0, 'books_count': 0, 'isbn': 700, 'isbn13': 585, 'authors': 0, 'original_publication_year': 21, 'original_title': 585, 'title': 0, 'language_code': 1084, 'average_rating': 0, 'ratings_count': 0, 'work_ratings_count': 0, 'work_text_reviews_count': 0, 'ratings_1': 0, 'ratings_2': 0, 'ratings_3': 0, 'ratings_4': 0, 'ratings_5': 0, 'image_url': 0, 'small_image_url': 0}

### Key Insights

1. **Data Completeness**: The dataset consists of 10,000 entries, but several key attributes, including `isbn`, `isbn13`, `original_publication_year`, and `original_title`, have significant missing values. This could impact analysis related to book identification and publication trends.

2. **Author Representation**: With 4,664 unique authors, Stephen King appears most frequently, indicating that a significant portion of popular books may be attributed to a limited number of authors.

3. **Average Ratings**: The average rating across books is approximately 4.0, with a standard deviation of 0.25, suggesting a generally positive reception from readers. There are only a handful of low ratings, which may warrant further examination.

4. **Outlier Presence**: Outliers are detected across multiple attributes, with the highest counts in `ratings_count`, `work_ratings_count`, and `work_text_reviews_count`. This suggests a range in user engagement, where some books are rated significantly more than others.

5. **Feature Importance**: The most important features for understanding the dataset include `work_ratings_count`, `ratings_count`, and `average_rating`, which heavily influence other metrics like user engagement and overall popularity of books.

### Dataset Overview

- **Total Entries**: 10,000
- **Key Columns**: The dataset includes identifiers, ratings, author information, language codes, and publication year.
- **Missing Values**: Several columns show substantial missingness, primarily `isbn`, `isbn13`, `original_publication_year`, and `original_title`.
- **Average Rating**: 4.00 with a standard deviation of 0.25.
- **Authors**: 4,664 unique authors are represented in the dataset.

### Key Findings

- **Publication Trends**: There are 21 missing entries in the `original_publication_year`, which needs to be addressed for a complete historical analysis.
- **Clustering Results**: K-Means clustering indicated distinct groupings within the dataset, potentially revealing differing characteristics among various subsets of books (e.g., bestsellers vs. lesser-known works).
- **Engagement Variability**: Disparities in user ratings and reviews point to a need for further investigation into audience preferences and behaviors. Notably, `work_text_reviews_count` showed significant variation.

### Recommendations

1. **Address Missing Data**: Determine strategies to handle missing values, particularly in key identifiers and publication years—considering methods like imputation or exclusion, as appropriate.

2. **Detailed Outlier Analysis**: Conduct deeper analyses of the outliers identified in user ratings and reviews to understand what differentiates these books and whether they impact the overall trends significantly.

3. **Engagement Strategies**: Since the dataset shows high variance in ratings and reviews, tailored marketing and engagement strategies could enhance visibility for lesser-known titles or authors, potentially bundling them with popular works.

4. **Temporal Analysis**: To draw more insights from the `original_publication_year`, filling in missing records or adjusting analyses to account for missing values will be crucial for understanding historical trends in book popularity.

### Conclusions 

The dataset provides a robust foundation for analyzing literacy trends, author popularity, and user engagement with literature. Despite notable challenges with missing data and outliers, the overall insights suggest a thriving landscape of diverse literature heavily influenced by a small cadre of prolific authors. Data cleaning and targeted analysis could unlock further valuable insights, potentially guiding publishing strategies and reader engagement moving forward.

### Outlier Detection Results
Detected outliers in 'book_id': 0 rows
Detected outliers in 'goodreads_book_id': 345 rows
Detected outliers in 'best_book_id': 357 rows
Detected outliers in 'work_id': 601 rows
Detected outliers in 'books_count': 844 rows
Detected outliers in 'isbn13': 556 rows
Detected outliers in 'original_publication_year': 1031 rows
Detected outliers in 'average_rating': 158 rows
Detected outliers in 'ratings_count': 1163 rows
Detected outliers in 'work_ratings_count': 1143 rows
Detected outliers in 'work_text_reviews_count': 1005 rows
Detected outliers in 'ratings_1': 1140 rows
Detected outliers in 'ratings_2': 1156 rows
Detected outliers in 'ratings_3': 1149 rows
Detected outliers in 'ratings_4': 1131 rows
Detected outliers in 'ratings_5': 1158 rows

### Feature Importance Analysis
|    | Feature                   |   Importance |
|---:|:--------------------------|-------------:|
|  9 | work_ratings_count        |  0.654384    |
|  8 | ratings_count             |  0.175535    |
|  0 | book_id                   |  0.0859777   |
| 14 | ratings_4                 |  0.0342186   |
|  7 | average_rating            |  0.0284366   |
| 10 | work_text_reviews_count   |  0.00505613  |
| 11 | ratings_1                 |  0.00386697  |
|  1 | goodreads_book_id         |  0.00239981  |
| 12 | ratings_2                 |  0.00218948  |
| 13 | ratings_3                 |  0.00189434  |
|  6 | original_publication_year |  0.00145861  |
|  4 | books_count               |  0.00143634  |
|  5 | isbn13                    |  0.0012705   |
|  3 | work_id                   |  0.00126954  |
|  2 | best_book_id              |  0.000606341 |

### Correlation Analysis
Correlation Matrix saved as C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads\correlation_matrix.png

### Clustering Analysis
K-Means clustering successfully performed with 3 clusters on numeric columns: ['book_id', 'goodreads_book_id', 'best_book_id', 'work_id', 'books_count', 'isbn13', 'original_publication_year', 'average_rating', 'ratings_count', 'work_ratings_count', 'work_text_reviews_count', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5']. Results plotted in two dimensions.

### Distribution Analysis
Boxplot created for book_id.
Boxplot created for goodreads_book_id.
Boxplot created for best_book_id.
Boxplot created for work_id.
Boxplot created for books_count.
Boxplot created for isbn13.
Boxplot created for original_publication_year.
Boxplot created for average_rating.
Boxplot created for ratings_count.
Boxplot created for work_ratings_count.
Boxplot created for work_text_reviews_count.
Boxplot created for ratings_1.
Boxplot created for ratings_2.
Boxplot created for ratings_3.
Boxplot created for ratings_4.
Boxplot created for ratings_5.

### Visualizations
![Correlation Heatmap](C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/correlation_heatmap.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/book_id_histogram.png](book_id_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/goodreads_book_id_histogram.png](goodreads_book_id_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/best_book_id_histogram.png](best_book_id_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/work_id_histogram.png](work_id_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/books_count_histogram.png](books_count_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/isbn13_histogram.png](isbn13_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/original_publication_year_histogram.png](original_publication_year_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/average_rating_histogram.png](average_rating_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/ratings_count_histogram.png](ratings_count_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/work_ratings_count_histogram.png](work_ratings_count_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/work_text_reviews_count_histogram.png](work_text_reviews_count_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/ratings_1_histogram.png](ratings_1_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/ratings_2_histogram.png](ratings_2_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/ratings_3_histogram.png](ratings_3_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/ratings_4_histogram.png](ratings_4_histogram.png)
![Histogram: C:\Users\Abdul Hadi\Desktop\TdsProject2\goodreads/ratings_5_histogram.png](ratings_5_histogram.png)
### Suggestions
Here are several analyses that could yield meaningful insights from the dataset you've summarized:

1. **Authors Analysis**:
   - Identify the most prolific authors by counting the number of books attributed to each author.
   - Analyze the average rating of books by each author to see if a correlation exists between the number of publications and average ratings.

2. **Publication Year Trends**:
   - Conduct a trend analysis of average ratings over the decades to see how reader preferences might have changed over time.
   - Explore the relationship between the year of original publication and ratings/review counts to determine if older books fare better or worse compared to newer publications.

3. **Language Code Insights**:
   - Analyze ratings and reviews by language code to identify which languages have the highest average ratings and engagement (ratings count and work ratings count).
   - Compare the number of books available in each language to their corresponding ratings and popularity.

4. **Rating Distribution**:
   - Visualize the distribution of ratings (ratings_1 to ratings_5) across different books to identify patterns in user responses.
   - Analyze the correlation between the distribution of ratings and average ratings.

5. **ISBN and Identifiers Analysis**:
   - Explore the impact of missing ISBN data on book discoverability and user ratings.
   - Group books by ISBN or ISBN13 to identify duplicates or variations in editions and their corresponding ratings.

6. **Book Count vs. Ratings**:
   - Analyze whether the number of books associated with a single title (as per the `books_count` column) has any impact on the ratings or reviews.
   - Compare books with a high number of versions to those with fewer versions to see if there is a noticeable difference in reader engagement.

7. **Visualizing Image URL Data**:
   - Count the frequency of different images associated with book entries to see if visually distinctive covers correlate with better ratings or engagement.

8. **User Engagement Metrics**:
   - Examine the relationships between `ratings_count`, `work_ratings_count`, `work_text_reviews_count`, and `average_rating` to understand how user engagement influences overall book perception.
   - Identify thresholds of engagement (e.g., minimum ratings counts) that correlate to significantly different average ratings.

9. **Book Popularity Trends**:
   - Use time series analysis to look at how the ratings or review counts change over time for specific popular books or authors.
   - Identify potential seasonal trends in book ratings, especially for specific genres if genre data is available through further exploration of titles.

10. **Missing Value Impact**:
    - Investigate how books with missing values in critical columns like `isbn`, `original_publication_year`, or `original_title` differ in ratings compared to those without missing values.

11. **Sentiment Analysis of Reviews**:
    - If text reviews were available, perform sentiment analysis to see if there are specific keywords or phrases that correlate with higher or lower ratings.

By conducting these analyses, you could derive valuable insights into user preferences, trends in literature, and the relationships between various book characteristics and user ratings/reviews. Each analysis could aid in understanding not only what makes a book successful but also how audience interactions with books might be evolving.

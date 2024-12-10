# Automated Data Analysis Report for Goodreads

## Dataset: goodreads.csv

### Dataset Overview
- **Columns**: ['book_id', 'goodreads_book_id', 'best_book_id', 'work_id', 'books_count', 'isbn', 'isbn13', 'authors', 'original_publication_year', 'original_title', 'title', 'language_code', 'average_rating', 'ratings_count', 'work_ratings_count', 'work_text_reviews_count', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5', 'image_url', 'small_image_url']
- **Missing Values**: {'book_id': 0, 'goodreads_book_id': 0, 'best_book_id': 0, 'work_id': 0, 'books_count': 0, 'isbn': 700, 'isbn13': 585, 'authors': 0, 'original_publication_year': 21, 'original_title': 585, 'title': 0, 'language_code': 1084, 'average_rating': 0, 'ratings_count': 0, 'work_ratings_count': 0, 'work_text_reviews_count': 0, 'ratings_1': 0, 'ratings_2': 0, 'ratings_3': 0, 'ratings_4': 0, 'ratings_5': 0, 'image_url': 0, 'small_image_url': 0}

### Key Insights

1. **Data Completeness**: The dataset has various missing values, especially in the `isbn`, `isbn13`, `original_publication_year`, `original_title`, and `language_code` columns, indicating incomplete data for several books.
  
2. **Average Ratings**: The average rating for the books is approximately 4.00, which reflects a generally positive reception among readers.

3. **Authors**: The dataset includes 4664 unique authors, with Stephen King being the most frequently mentioned author, appearing 60 times.

4. **Language Diversity**: The dataset has entries in 25 unique languages, with English (identified by code 'eng') being the most prevalent.

5. **Outliers**: Multiple numeric columns show the presence of outliers. This could affect analyses such as average ratings and ratings counts, skewing perceived trends.

6. **Clustering**: The successful application of K-Means clustering on the dataset revealed three distinct clusters, which can help in segmenting the books for targeted analyses and recommendations.

### Dataset Overview

- **Size**: The dataset contains a total of 10,000 entries with 21 feature columns.
- **Missing Values**: Several columns such as `isbn`, `original_publication_year`, and `language_code` exhibit substantial missing data.
- **Data Types**: The dataset includes categorical features (e.g., `authors`, `language_code`, etc.) as well as numeric features (e.g., `average_rating`, `ratings_count`, etc.).

### Key Findings

1. **Distribution of Ratings**: 
   - The ratings distribution shows high counts for higher ratings (ratings 4 and 5) compared to lower ratings (ratings 1, 2, and 3).
   - There are significant numbers of books receiving a very high number of ratings, indicating popularity among certain titles.

2. **Trends in Publication Years**: 
   - The `original_publication_year` variable has outliers, including very old publication years, which implies historical text inclusion.

3. **Feature Importance**:
   - The most influential features for determining ratings and book popularity include `work_ratings_count`, `ratings_count`, and `average_rating`.

### Recommendations

1. **Data Cleaning**: Address the missing values, particularly in the `isbn`, `original_publication_year`, and `original_title` columns. Consider imputation strategies or removal of these entries as appropriate.

2. **Outlier Analysis**: Investigate outliers further to determine if they represent valid exceptional cases or errors that should be cleaned from the dataset.

3. **Expand Language Data**: Enhance the language diversity by sourcing more entries in underrepresented languages to increase the usability of the dataset.

4. **Use Clustering for Marketing**: Employ the clustering results for more targeted marketing strategies, focusing on the unique traits of each cluster in book recommendations.

5. **Periodic Updates**: Regularly refresh the dataset with new book entries and reviews to maintain relevance and accuracy in trends.

### Conclusions

The dataset provides a wealth of information regarding books, authors, and reader preferences, though it requires some cleanup and enrichment. The positive average ratings reflect well on the dataset's overall quality, suggesting a collection of beloved titles. Further explorations, particularly concerning outliers and missing values, alongside the outlined recommendations, can significantly enhance both the quality of the dataset and its applications. By leveraging the insights garnered through analyses such as clustering and feature importance, stakeholders can refine their approaches towards book selection, marketing, and reader engagement strategies.

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

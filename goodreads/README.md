# Automated Data Analysis Report for Goodreads

## Dataset: goodreads.csv

### Dataset Overview
- **Columns**: ['book_id', 'goodreads_book_id', 'best_book_id', 'work_id', 'books_count', 'isbn', 'isbn13', 'authors', 'original_publication_year', 'original_title', 'title', 'language_code', 'average_rating', 'ratings_count', 'work_ratings_count', 'work_text_reviews_count', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5', 'image_url', 'small_image_url']
- **Missing Values**: {'book_id': 0, 'goodreads_book_id': 0, 'best_book_id': 0, 'work_id': 0, 'books_count': 0, 'isbn': 700, 'isbn13': 585, 'authors': 0, 'original_publication_year': 21, 'original_title': 585, 'title': 0, 'language_code': 1084, 'average_rating': 0, 'ratings_count': 0, 'work_ratings_count': 0, 'work_text_reviews_count': 0, 'ratings_1': 0, 'ratings_2': 0, 'ratings_3': 0, 'ratings_4': 0, 'ratings_5': 0, 'image_url': 0, 'small_image_url': 0}

### Key Insights
1. **Missing Data**: Significant missing values exist in the `isbn`, `isbn13`, `original_publication_year`, `original_title`, and `language_code` columns, indicating potential issues with data collection or entry.
2. **Outlier Presence**: Many columns have detected outliers, particularly in `ratings_count`, `work_ratings_count`, and rating distributions. This could skew analysis and insights.
3. **Feature Importance**: The most influential features impacting ratings are `work_ratings_count` and `ratings_count`, suggesting their direct correlation with user engagement and book rating.
4. **Author Popularity**: The dataset has 4664 unique authors, with Stephen King being the most frequently mentioned, indicating potential focus areas for genre or author-specific analyses.

### Dataset Overview
- The dataset contains **10,000 books** with various attributes including ratings, authors, publication years, and different identifiers.
- **Key Columns**: Include identifiers (`book_id`, `goodreads_book_id`), `authors`, `average_rating`, `ratings_count`, as well as publication information (`original_publication_year`, `language_code`).
- **Missing Entries**: Out of the 10,000 records, several columns have considerable missing values:
  - `isbn` (700 missing)
  - `isbn13` (585 missing)
  - `original_publication_year` (21 missing)
  - `original_title` (585 missing)
  - `language_code` (1,084 missing)

### Key Findings
1. **Statistical Analysis**: The average rating across books is approximately **4.00**, with a standard deviation of about **0.25**, indicating a generally favorable reception among readers.
2. **Rating Distribution**: Outlier detection suggests that many ratings may not represent typical user experiences, especially at the extremes (e.g., very high or very low ratings).
3. **Concentration of Ratings**: Significant concentration of ratings in just a few categories (e.g., `ratings_5`, `ratings_4`), which indicates possible bias or popularity dynamics influencing ratings.
4. **Publication Trends**: Original publication years span historically back to **1750**, reflecting a wide range of literary contributions over centuries.

### Recommendations
1. **Data Cleaning**: Address missing values rigorously, possibly imputing for `isbn`, `isbn13`, and `original_title`, or utilizing techniques to handle missing data effectively.
2. **Outlier Treatment**: Consider analyzing data subsets without outliers to ensure results are robust and representative of typical book performance.
3. **Author and Genre Focus**: Leverage the popularity of particular authors like Stephen King for targeted promotions or focuses in book recommendations.
4. **Further Analysis on Language**: Investigate the impact of different language codes on book ratings and user engagement, given the missing values in this column.

### Conclusions
The dataset offers a comprehensive overview of books, their ratings, and associated metadata that can inform decision-making for libraries, publishers, or even readers seeking high-quality recommendations. However, careful attention must be paid to missing values and outliers, as these could distort insights and lead to suboptimal conclusions. Focusing on rigorous data validation and potentially enriching the dataset through additional sources could lead to deeper and more actionable insights.

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

### Correlation Heatmap
![Correlation Heatmap](C:\Users\Abdul Hadi\Desktop\TdsProject2\TDSProject2\goodreads/correlation_heatmap.png)

### Boxplots
![Boxplot](C:\Users\Abdul Hadi\Desktop\TdsProject2\TDSProject2\goodreads/book_id_boxplot.png)

![Boxplot](C:\Users\Abdul Hadi\Desktop\TdsProject2\TDSProject2\goodreads/goodreads_book_id_boxplot.png)

![Boxplot](C:\Users\Abdul Hadi\Desktop\TdsProject2\TDSProject2\goodreads/best_book_id_boxplot.png)

### Histograms
![Histogram](C:\Users\Abdul Hadi\Desktop\TdsProject2\TDSProject2\goodreads/book_id_histogram.png)

![Histogram](C:\Users\Abdul Hadi\Desktop\TdsProject2\TDSProject2\goodreads/goodreads_book_id_histogram.png)

![Histogram](C:\Users\Abdul Hadi\Desktop\TdsProject2\TDSProject2\goodreads/best_book_id_histogram.png)

## Suggestions

The dataset you provided contains a wealth of information about books, including their ratings, authors, publication years, and more. Here are several analyses that could yield meaningful insights:

1. **Authors' Popularity Analysis:**
   - Determine the most popular authors based on the number of books published and the average ratings of their works. This could involve aggregating the number of books and average ratings by author.

2. **Book Ratings Distribution:**
   - Analyze the distribution of ratings (1 to 5 stars) across different books. This could involve creating histograms or box plots to visualize how ratings are spread and identifying any outlier ratings or trends.

3. **Publication Trends Over Time:**
   - Investigate the trend of book publications over the years. Are more books being published in recent years? You could visualize the number of books published per year and look for significant changes over decades.

4. **Language Analysis:**
   - Analyze the distribution of books by language code. Identify the most common languages and how ratings compare across different languages.

5. **Impact of Ratings on Average Rating:**
   - Examine the relationship between the total number of ratings (`ratings_count`) and the average rating (`average_rating`). Use correlation analysis to see if there's a significant relationship between the two.

6. **Text Review Analysis:**
   - Analyze the correlation between the number of text reviews (`work_text_reviews_count`) and average ratings. This could help understand if more reviews correlate with higher or lower ratings.

7. **ISBN and ISBN13 Completeness:**
   - Investigate the missing values in the `isbn` and `isbn13` columns to understand their impact on data integrity. You might find patterns in missing data based on certain subsets of books (e.g., older publications).

8. **Rating Trends by Publication Year:**
   - Compare the average ratings across different ranges of publication years to see if older books tend to be rated higher or lower than more recent books.

9. **Comparison of Top Rated Books:**
   - Identify the top-rated books based on `average_rating` and analyze if they share common attributes (like the number of ratings, authors, publication years, etc.).

10. **Book Count Analysis:**
    - Use the `books_count` column to identify prolific authors or series and analyze their average ratings in comparison to books with fewer entries.

11. **Visualizing Relationships:**
    - Create scatter plots or pair plots to visualize the relationships between various numeric features (like `average_rating`, `ratings_count`, `work_ratings_count`, etc.) and assess potential correlations.

12. **Image URLs Analysis:**
    - Analyze the distribution of the most common book cover images and see if certain styles correlate with higher ratings.

13. **Top Genres or Categories:**
    - If the dataset has implicit or explicit genre categorization (possibly through author or title analysis), identify which genres have the highest average ratings.

14. **Missing Data Analysis:**
    - Analyze the impact of the missing values in 'original_publication_year' and 'original_title' on your overall analysis to understand how these gaps may bias insights you draw from the dataset.

15. **Outlier Detection:**
    - Use statistical methods to detect outliers in the ratings or review counts. Outliers can signify unique books that are exceptionally rated or widely panned.

These analyses can be conducted separately or combined in various ways to glean deeper insights, patterns, and trends from the data. Additionally, utilizing data visualization tools will help in communicating the findings effectively.


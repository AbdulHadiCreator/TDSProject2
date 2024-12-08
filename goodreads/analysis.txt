# Automated Data Analysis Report for Goodreads

## Dataset: goodreads.csv

### Basic Analysis
- Columns: ['book_id', 'goodreads_book_id', 'best_book_id', 'work_id', 'books_count', 'isbn', 'isbn13', 'authors', 'original_publication_year', 'original_title', 'title', 'language_code', 'average_rating', 'ratings_count', 'work_ratings_count', 'work_text_reviews_count', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5', 'image_url', 'small_image_url']
- Missing Values: {'book_id': 0, 'goodreads_book_id': 0, 'best_book_id': 0, 'work_id': 0, 'books_count': 0, 'isbn': 700, 'isbn13': 585, 'authors': 0, 'original_publication_year': 21, 'original_title': 585, 'title': 0, 'language_code': 1084, 'average_rating': 0, 'ratings_count': 0, 'work_ratings_count': 0, 'work_text_reviews_count': 0, 'ratings_1': 0, 'ratings_2': 0, 'ratings_3': 0, 'ratings_4': 0, 'ratings_5': 0, 'image_url': 0, 'small_image_url': 0}

### Key Insights
### Dataset Analysis Story

#### Overview
The dataset comprises 10,000 entries with detailed information about various books, including unique identifiers, authors, publication details, language, ratings, and counts of reviews. Key columns analyzed include `book_id`, `average_rating`, `ratings_count`, and author information.

#### Key Findings

1. **Data Completeness**:
   - The dataset is generally robust, with most fields complete. However, several columns exhibit missing values:
     - ISBN numbers (700 missing)
     - ISBN13 (585 missing)
     - Original publication years (21 missing)
     - Original titles (585 missing)
     - Language codes (1084 missing)
   - The absence of the `isbn` and `isbn13` values may hinder the identification of specific editions, which could affect market analysis.

2. **Author Insights**:
   - The dataset features 4,664 unique authors, with Stephen King being the most frequently mentioned (60 occurrences). This popularity suggests a strong interest in his works, an insight that could guide market focus for promotions or inventory decisions.

3. **Publication Trends**:
   - The majority of books were published around the early 2000s, with a mean publication year of approximately 1982. However, years as far back as -1750 indicate variability in entries, likely representing reprints or compilations. This historical range may influence the book's thematic relevance today.

4. **Rating Analysis**:
   - The average rating across all books is 4.00, with ratings mostly clustering between 3.85 and 4.18 for the 25th to 75th percentiles. This suggests that most readers find the books in this dataset quite favorable, indicating a positive quality perception.
   - Ratings distribution shows a significant count for each rating category from 1 to 5, with higher ratings (4 and 5) being the most frequent. This can be seen as encouragement for authors/publishers about the audience's positive reception.

5. **Language Distribution**:
   - Most books (approximately 89.16%) are in English, which is significant for targeting strategies and marketing initiatives. The diverse range of languages (25 unique codes) implies opportunities for multilingual editions.

6. **Review Dynamics**:
   - The average count of work text reviews is 2,919. This suggests reader engagement and the potential for community interaction around book discussions, which could be leveraged for promotional campaigns.

7. **Correlation Insights**:
   - Correlation heatmaps could reveal relationships between variables, such as a potential positive correlation between `ratings_count` and `average_rating`. High-rated books tend to have more ratings, suggesting that quality drives reader engagement.

#### Recommendations

1. **Address Missing Values**:
   - Devise strategies to handle missing data, especially in essential columns like ISBN. Consider using data imputation or leveraging related datasets to fill in gaps.

2. **Focus on Popular Authors**:
   - Develop marketing campaigns centered around popular authors, particularly those with multiple titles in the dataset, to maximize visibility.

3. **Promote Highly Rated Books**:
   - Foster reader engagement by employing social media and community interaction to promote books with high average ratings, potentially leveraging user-generated content as a marketing tool.

4. **Encourage Multilingual Editions**:
   - For the language variations present, consider translating popular titles into other languages to broaden market reach and inclusivity.

5. **Utilize Reader Reviews**:
   - Encourage more in-depth reviews and feedback from readers, perhaps through incentives, as high engagement can bolster book visibility and attractiveness to potential readers.

6. **Explore Historical Context**:
   - Investigate older publications that still receive readership to understand what continues to engage readers, potentially identifying trends for future book selections.

#### Conclusion
This dataset provides a robust foundation for understanding book market trends and consumer preferences. By addressing the identified gaps and leveraging existing strengths, stakeholders can enhance their strategies for both marketing and inventory development, ensuring they align with reader preferences and market demands.

### Visualizations
![Correlation Heatmap](correlation_heatmap.png)
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

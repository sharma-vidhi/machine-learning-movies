# Movie Recommendation Engine

Predictive engine for recommending movies to users based on their likeness.

## Data used

 [Movie Lense 100k](https://grouplens.org/datasets/movielens/100k/)
 
 ```
 * u.data: 100000 ratings by 943 users on 1682 items - user id | item id | rating | timestamp 
 * u.item: List of the movies - movie id | movie title | release date | video release date |IMDb URL | unknown | Action | Adventure | Animation |Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western |
 * u.genre: List of the genres
 * u.user: Demographic information about the users - user id | age | gender | occupation | zip code
 * u.occupation: List of the occupations
 ```

## Algorithms Used
 ```
 * K-means
 * GMM
 * Decision Tree
 * Logistic Regression
 * Support Vector Machine
 * Naive Bayes
 * Random Forrest
 ```
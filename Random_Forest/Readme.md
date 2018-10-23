## Dataset
IMDB Movie Dataset. This dataset is generated from IMDb data. The dataset is released under Open Database License and has rights to use granted under some conditions. The dataset is enriched with various details of 5000 different language movies and can be used for practical business scenarios. 
<br><br>The link of the dataset is here - (https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset).

## Objective
What role does the attributes of a movie such as genres and duration affect the user ratings 
### Prepare the data for algorithm
1.	Load the dataset in a pandas dataframe and analyze the data.
2.	#### Data Cleaning: 
    Remove the noise and drop the rows with null or garbage values
3.	#### Data Preparation: 
    The attribute ‘Genres’ had many strings, separate each string into an individual feature to inspect it. Used pandas.get_dummies to achieve this.
	
  ##### Sklearn OneHotEncoding vs Pandas get_dummies:
       OneHotEncoder cannot process string values directly. If your nominal features are strings, then you need to first map them into integers.
	
       pandas.get_dummies is kind of the opposite. By default, it only converts string columns into one-hot representation, unless columns are specified

4.	Now data for exploration only has movie characteristics. Next is processing imdb_score which ranges from 1 to 10, wrote a python function which 1 to 10 values – 1 to 5 with 1,2 being 1; 3,4 being 2 so on and so forth.
5.	Split the data into train and test set, where 20% is for testing and 80% is training data.
## Algorithm
### Decision Tree
* Used 25 different features in the dataset for Decision Tree with gini index with maximum depth as 15. 
* The decision tree classifier gives a comprehensive analysis of the consequences of each possible decision, such as what the decision leads to, whether it ends in uncertainty or a definite conclusion, or whether it leads to new issues for which the process needs repetition.

#### Entropy: 
A common measure of target class impurity
#### Entropy=Σi–pilog2pi
#### Gini: 
Gini Impurity is another measure of impurity
#### Gini=1–Σip2i
#### Decision Tree Classifier Accuracy score: 0.580 or 58%
Plot the tree for visualization.
### Random Forest
* Used sklearn.datasets.make_classification with n_samples=1000, n_features=6, n_informative=5 and n_redundant=0 which creates multiclass datasets by allocating each class one or more normally-distributed clusters of points. It specialises in introducing noise by way of: correlated, redundant and uninformative features; multiple Gaussian clusters per class; and linear transformations of the feature. 
* Split the obtained dataset into 80% training data and 20% test data.
* Create a Random Forest Classifier with n_estimators=1000 and max_depth=6

#### Random Forest Accuracy score: 0.935 or 93% 

    Since the dimensions are huge, principal component analysis can help in reducing the curse of dimensionality. 
### PCA    
   * Create 2 attributes – principal component1 and principal component 2. 
   * Applied the same decision tree algorithm to check the results. 
   * Accuracy score: .556 or 55%

### Naïve Bayes
* Used the components obtained from principal component analysis i.e principal component 1 and principal component 2 to apply naïve bayes algorithm.
#### Naive Bayes Accuracy Score: .604 or 60%

## Conclusion
Principal Component Analysis does not always improve the accuracy of the model but it is advisable as it improves the performance of the model
## New Insights
Random forest gives good accuracy which is very high, suspecting that the model might be overfitting caused by over growing trees. Feature engineering is required for the training dataset.




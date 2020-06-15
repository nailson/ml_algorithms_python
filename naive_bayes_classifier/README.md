# Naive Bayes Classifier

Naive Bayes is a probabilistic Classifier that used Bayes theorem to calcuçate probabilities and conditional probabilities.

* Bernoulli

Binomial variables where all features are binary (have two classes). For example Genre, contains word in document, etc.

* Multinomial

Categorical features, such as Outlook (Sunny, Cloudy, Raining, etc.), counting of words in a document, etc.

* Gaussian

Assumes that the feature follow a normal distribution, such as height, temperature, etc.

## Probabilistic Model

For this demonstration we will use go-out.csv dataset:

| Weather 	| Car 	| Class 	| predictions 	| Wind 	| Play 	| predictions 	|   	|
|--------:	|----:	|------:	|------------:	|-----:	|-----:	|------------:	|---	|
|       0 	|   1 	|     1 	|           1 	|    1 	|    0 	|           0 	| 0 	|
|       1 	|   0 	|     0 	|           1 	|    0 	|    0 	|           0 	| 0 	|
|       2 	|   1 	|     1 	|           1 	|    1 	|    0 	|           1 	| 1 	|
|       3 	|   1 	|     1 	|           1 	|    1 	|    0 	|           1 	| 1 	|
|       4 	|   1 	|     1 	|           1 	|    1 	|    0 	|           1 	| 1 	|
|       5 	|   0 	|     0 	|           0 	|    0 	|    0 	|           0 	| 1 	|
|       6 	|   0 	|     0 	|           0 	|    0 	|    0 	|           1 	| 1 	|
|       7 	|   1 	|     1 	|           0 	|    1 	|    0 	|           0 	| 0 	|
|       8 	|   1 	|     0 	|           0 	|    0 	|    0 	|           1 	| 1 	|
|       9 	|   0 	|     0 	|           0 	|    0 	|    0 	|           1 	| 1 	|

### Calculate the Prior
Calculate the Prior Probabilities
P(Class=1) = count(Class==1)/count(Class==1)+count(Class==0)
P(Class=0) = count(Class==0)/count(Class==0)+count(Class==1)

### Calculate the Likelihood

Calculate the Likelihood

#### Weather

* P( Weather = 1 | Class = 1) = count( Weather = 1 and Class = 1) / count(Class = 1)
* P( Weather = 0 | Class = 1) = count( Weather = 0 and Class = 1) / count(Class = 1)
* P( Weather = 1 | Class = 0) = count( Weather = 1 and Class = 0) / count(Class = 0)
* P( Weather = 0 | Class = 0) = count( Weather = 0 and Class = 0) / count(Class = 0)

#### Car

* P( Car = 1 | Class = 1) = count( Car = 1 and Class = 1) / count(Class = 1)
* P( Car = 0 | Class = 1) = count( Car = 0 and Class = 1) / count(Class = 1)
* P( Car = 1 | Class = 0) = count( Car = 1 and Class = 0) / count(Class = 0)
* P( Car = 0 | Class = 0) = count( Car = 0 and Class = 0) / count(Class = 0)

### Predictions


## Advantages

* Good results with a small data to train the model
* Highly Scalable
* Quick to train and update (linear)
* Probabilities as output
* Light to Run (CPU and Ram)

## Weaknesses

* Strong Independence Assumption between features
* Performance is very sensitive to skewed data

## References

[Machine Learning Mastery Book](https://machinelearningmastery.com/master-machine-learning-algorithms/)
[Naive Bayes Tutorial: Naive Bayes Classifier in Python](https://dzone.com/articles/naive-bayes-tutorial-naive-bayes-classifier-in-pyt)
[Naive Bayes Classifier From Scratch](https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/)
[Mathematics Behind Naive Bayes](https://heartbeat.fritz.ai/understanding-the-mathematics-behind-naive-bayes-ab6ee85f50d0)
[Naive Bayes Classifier With Example](https://www.youtube.com/watch?v=l3dZ6ZNFjo0)
[Naive Bayes Algorithm](https://www.youtube.com/watch?v=vz_xuxYS2PM)
[Naive Bayes Explained](https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/)

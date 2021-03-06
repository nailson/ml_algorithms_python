# Naive Bayes Classifier

## Bayes Inference

![Bayes Rule](images/Bayes_rule.png)

* **Prior** - The prior distribution characterizes what is known about an unknown quantity before observing the data from the present study.
* **Likelihood** - The information in the observed data, and is used to update prior distributions to posterior distributions (How likely the evidence c comes from x distribution)
* **Posterior** - given the data (evidence)

## Naive Bayes Types

Naive Bayes is a probabilistic Classifier that used Bayes theorem to calculate probabilities and conditional probabilities. The most common Naive Bayes are:

* **Bernoulli**: Binomial variables where all features are binary (have two classes). For example Genre, contains word in document, etc.

* **Multinomial**: Categorical features, such as Outlook (Sunny, Cloudy, Raining, etc.), counting of words in a document, etc.

* **Gaussian**: Assumes that the feature follow a normal distribution, such as height, temperature, etc.

* **Others**: Beta, Theta, T-student. Different distributions could be used to model the feature behaviour.

>
## Probabilistic Model

For this demonstration we will use go-out.csv dataset:

<div style="max-width: 300px">

| Weather 	| Car 	| Class 	|
|:-:	|:-:	|:-:	|
| 1 	| 1 	| 1 	|
| 0 	| 0 	| 1 	|
| 1 	| 1 	| 1 	|
| 1 	| 1 	| 1 	|
| 1 	| 1 	| 1 	|
| 0 	| 0 	| 0 	|
| 0 	| 0 	| 0 	|
| 1 	| 1 	| 0 	|
| 1 	| 0 	| 0 	|
| 0 	| 0 	| 0 	|
</div>

### Calculate the Prior

Calculate the Prior Probabilities
* P(Class=1) = count(Class==1) / (count(Class==1) + count(Class==0))
* P(Class=0) = count(Class==0) / (count(Class==0) + count(Class==1))

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

### Calculate the Posterior (Predictions)


## Advantages

* Good results with a small data to train the model
* Highly Scalable
* Quick to train and update (linear)
* Probabilities as output
* Light to Run (CPU and Ram)
* Can be used for both binary and multi-class classification problems

## Weaknesses

* Strong Independence Assumption between features (In real life it's very difficult that the features are independent with each other)
* Performance is very sensitive to skewed data
* If a categorical variable has a category in the test dataset, which was not observed in training dataset, then the model will assign a 0 (zero) probability and will be unable to make a prediction.

## References

[Machine Learning Mastery Book](https://machinelearningmastery.com/master-machine-learning-algorithms/)

[Naive Bayes Tutorial: Naive Bayes Classifier in Python](https://dzone.com/articles/naive-bayes-tutorial-naive-bayes-classifier-in-pyt)

[Naive Bayes Classifier From Scratch](https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/)

[Mathematics Behind Naive Bayes](https://heartbeat.fritz.ai/understanding-the-mathematics-behind-naive-bayes-ab6ee85f50d0)

[Naive Bayes Classifier With Example](https://www.youtube.com/watch?v=l3dZ6ZNFjo0)

[Naive Bayes Algorithm](https://www.youtube.com/watch?v=vz_xuxYS2PM)

[Naive Bayes Explained](https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/)

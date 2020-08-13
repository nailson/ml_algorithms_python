# Linear Regression

To simplify, Linear Regression is simply a weighted sum of inputs plus a constant:

<img src="https://render.githubusercontent.com/render/math?math=\hat{y}%20=%20\beta_{0}%20%2B%20\beta_{1}x_1%20%2B%20\beta_{2}x_2%20%2B%20...%20%2B%20\beta_{n}x_n">

## Simple Linear Regression

Creating a simple one dimentional function of a linear relation between X and y:

<img src="https://render.githubusercontent.com/render/math?math=\hat{y}%20=%20\beta_{0}%20%2B%20\beta_{1}x_1"/>

</br>
<img src="images/regressionresidual.gif" width="250"/>


### Minize the residual sum of Squares

The residual sum of squares (RSS) is:

<img src="images/rss.png" width="220"/>
</br>
Using the e in i position represents the ith residual. The RSS is:


<img src="images/RSS2.png" width="550"/>

### Using Derivatives

Using derivatives to minimize the RSS we end up with this formula:

<img src="images/simple_parameters.png" width="220"/>

And, that it! we now can use the Betha1 as the slope and the Betha0 as the intercept.

## Multiple Linear Regression


## Gradient Descendent
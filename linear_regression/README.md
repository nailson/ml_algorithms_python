# Linear Regression

To simplify, Linear Regression is simply a weighted sum of inputs plus a constant:

<img src="https://render.githubusercontent.com/render/math?math=\hat{y}%20=%20\beta_{0}%20%2B%20\beta_{1}x_1%20%2B%20\beta_{2}x_2%20%2B%20...%20%2B%20\beta_{n}x_n">

## Simple Linear Regression

Creating a simple one dimentional function of a linear relation between X and y:

<img src="https://render.githubusercontent.com/render/math?math=\hat{y}%20=%20\beta_{0}%20%2B%20\beta_{1}x_1"/>

</br>
<img src="images/regressionresidual.gif" width="250"/>


### Minimize the residual sum of Squares

The residual sum of squares (RSS) is:

<img src="images/rss.png" width="220"/>
</br>
Using the e in i position represents the ith residual. The RSS is:


<img src="images/RSS2.png" width="550"/>

### Using Derivatives

Using derivatives to minimize the RSS 

<img src="images/contour_simple_rss.png" width="550"/>

we end up with this formula:

<img src="images/simple_parameters.png" width="220"/>

And, that it! we now can use the Betha1 as the slope and the Betha0 as the intercept.

### Analysing the residuals

How accurate is the sample mean ˆμ as an estimate of μ?

By calculate the standard error of each parameter Betha0 and Betha1 :

<img src="images/residuals_analysis.png" width="520"/>

The Sigma is the standard error of the residuals (or residual standard error RSE) Y - ^Y and can be retrieved by this formula:

<img src="images/sd_residuals.png" width="180"/>

### Residuals Assumptions

The error term or residuals assume to be:

* Normally distributed
* Homoscedastic (same variance for every X)
* Independent

## Multiple Linear Regression


## Gradient Descendent

## References

[Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning. ](https://doi.org/10.1007/b94608_4)

[Regression & Correlation for Military Promotion: A Tutorial](https://www.kdnuggets.com/2016/04/regression-correlation-military-tutorial.html/2)

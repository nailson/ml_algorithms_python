import numpy as np


class LeastSquaresRegression():

    def __init__(self):
        self.intercept = None
        self.slope = None

    def fit(self, X, y):

        def deviation(array):
            return [x-np.mean(array) for x in array]

        def squared_deviation(array):
            return [(x-np.mean(array))**2 for x in array]

        def least_squares_fit(X, y):
            numerator = np.sum([x_dev*y_dev for x_dev, y_dev in zip(deviation(X), deviation(y))])
            denominator = np.sum(squared_deviation(X))
            slope = numerator/denominator
            
            intercept = np.mean(y) - slope * np.mean(X)

            return intercept, slope

        self.intercept, self.slope = least_squares_fit(X, y)

        return None

    def predict(self, X):
        y_pred = self.intercept + (X * self.slope)

        return y_pred

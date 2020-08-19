import numpy as np


class LeastSquaresRegression():

    def __init__(self):
        self.coef = None

    def fit(self, X, y):

        def least_squares_fit(X, y):

            # add x0 = 1 (intercept) to each instance
            X_b = np.c_[np.ones((100, 1)), X.values]

            # Apply the normal formula using matrix transformations
            theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y.values)

            return theta_best

        self.coef = least_squares_fit(X, y)

        return None

    def predict(self, X):

        X_b = np.c_[np.ones((100, 1)), X.values]
        y_pred = X_b.dot(self.coef)

        return y_pred

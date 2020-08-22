import numpy as np


class LeastSquaresRegression():

    def __init__(self):
        self.coef = None

    def fit(self, X, y, gradient_descendent=False):
        def gradient_descendent_fit(X, y, n_iterations=1000, learning_rate=0.1):
            theta = np.random.randn(2, 1)  # random initialization
            X_b = np.c_[np.ones((100, 1)), X.values]   # add x0 = 1 (intercept) to each instance

            for _ in range(n_iterations):
                gradients = 2/len(X) * X_b.T.dot(X_b.dot(theta) - y.values)
                theta = theta - learning_rate * gradients

            return theta

        def least_squares_fit(X, y):
            X_b = np.c_[np.ones((100, 1)), X.values]  # add x0 = 1 (intercept) to each instance
            theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y.values)  # Apply the normal formula

            return theta_best

        self.coef = gradient_descendent_fit(X, y) if (gradient_descendent) else least_squares_fit(X, y)

        return None

    def predict(self, X):
        X_b = np.c_[np.ones((100, 1)), X.values]
        y_pred = X_b.dot(self.coef)

        return y_pred

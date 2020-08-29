import numpy as np


class LeastSquaresRegression():

    def __init__(self):
        self.coef = None

    def fit(self, X, y, gradient_descent=False, regularization=''):
        def gradient_descent_fit(X, y, n_iterations=1000, learning_rate=0.1):
            theta = np.random.randn(2, 1)  # random initialization
            X_b = np.c_[np.ones((100, 1)), X.values]   # add x0 = 1 (intercept) to each instance

            for _ in range(n_iterations):
                gradients = 2/len(X) * X_b.T.dot(X_b.dot(theta) - y.values)
                theta = theta - learning_rate * gradients

            return theta

        def ridge_fit(X, y, alpha=0.1):
            X_b = np.c_[np.ones((100, 1)), X.values]  # add x0 = 1 (intercept) to each instance
            I_ = np.identity(X_b.shape[1])  # identity matrix
            theta_best = np.linalg.inv(X_b.T @ X_b + alpha*I_) @ X_b.T @ y  # Apply the normal formula

            return theta_best

        def lasso_fit(X, y, alpha=0.1):
            X_b = np.c_[np.ones((100, 1)), X.values]  # add x0 = 1 (intercept) to each instance
            theta_best = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y - alpha)

            return theta_best

        if gradient_descent:
            return gradient_descent_fit(X, y)
        elif regularization == '':
            return ridge_fit(X, y, alpha=0)
        elif regularization == 'l2':
            return ridge_fit(X, y)
        elif regularization == 'l1':
            return lasso_fit(X, y)

        return None

    def predict(self, X):
        X_b = np.c_[np.ones((100, 1)), X.values]
        y_pred = X_b.dot(self.coef)

        return y_pred

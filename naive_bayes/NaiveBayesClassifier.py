from operator import itemgetter
import numpy as np
import math


class NaiveBayesMultinomial():

    def __init__(self):
        self.prior_dict = {}
        self.likelyhood_dict = {}
        self.results = []

    def fit(self, X, y):
        # For each Class in y
        for c in y.unique():
            # Calculate the pior and store in the prior_dict dictionary
            self.prior_dict.update({c: {"prior": np.mean(y == c), "count": np.count_nonzero(y == c)}})

            # For each feature into X
            for col_name, feature_series in X.iloc[np.where(y == c)].iteritems():
                # If type is numerical
                if(str(feature_series.dtype) in ['int64', 'double']):
                    pass
                else:
                    # For each class into feature
                    for feature_c in X[col_name].unique():
                        # Calculate the Likelihood for each pair (Feature= feature class | Class = c)
                        # P(Weather=1|Class=1) = 0.8 and P(Weather=0|Class=1) = 0.2
                        if col_name not in self.likelyhood_dict.keys():
                            self.likelyhood_dict.update({
                                col_name: {
                                    (feature_c, c):
                                        np.count_nonzero(feature_series == feature_c) / len(feature_series)
                                }
                            })
                        else:
                            self.likelyhood_dict[col_name].update({
                                (feature_c, c):
                                    np.count_nonzero(feature_series == feature_c) / len(feature_series)
                            })

        return None

    def calculate_posterior(self, X):
        posterior_dict = []
        for c in list(self.prior_dict.keys()):
            # Initialize posterior as prior
            posterior = self.prior_dict[c]['prior']
            for col_name in X.index:
                # Naive assumption (independence):
                # P(x1,x2,x3|Y) = P(x1|Y)*P(x2|Y)*P(x3|Y)
                # Posterior is product of prior and likelihoods (ignoring scaling factor)
                if(type(X[col_name]) in [int, float, np.int64, np.float]):
                    pass
                else:
                    posterior *= self.likelyhood_dict[col_name][(X[col_name], c)]
            posterior_dict.append((c, posterior))

        return posterior_dict

    def predict(self, X):
        # For row in dataset
        self.results = [self.calculate_posterior(row) for index, row in X.iterrows()]

        return [max(prob, key=itemgetter(1))[0] for prob in self.results]


class NaiveBayesGaussian():

    def __init__(self):
        self.prior_dict = {}
        self.likelyhood_dict = {}
        self.results = []

    def calculate_gaussian_prob(self, x, colname, c):
        mean = self.likelyhood_dict[colname][c]['mean']
        sd = self.likelyhood_dict[colname][c]['mean']
        low_number = 1e-6  # prevent division by zero

        # Gaussian PDF to calculate the probability of a relative likelihood
        # that the value of the random variable x would equal that sample (mean and sd)
        coeff = 1.0 / math.sqrt(2.0 * math.pi * sd + low_number)
        exponent = math.exp(-(math.pow(x - mean, 2) / (2 * sd + low_number)))
        return coeff * exponent

    def fit(self, X, y):
        # For each Class in y
        for c in y.unique():
            # Calculate the pior and store in the prior_dict dictionary
            self.prior_dict.update({c: {"prior": np.mean(y == c), "count": np.count_nonzero(y == c)}})

            # For each feature into X
            for col_name, feature_series in X.iloc[np.where(y == c)].iteritems():
                # If type is numerical
                if(str(feature_series.dtype) in ['int64', 'double']):
                    if col_name not in self.likelyhood_dict.keys():
                        self.likelyhood_dict.update({
                            col_name: {
                                c: {"mean": np.mean(feature_series), "sd": np.std(feature_series)}
                            }
                        })
                    else:
                        self.likelyhood_dict[col_name].update({
                            c: {"mean": np.mean(feature_series), "sd": np.std(feature_series)}
                        })

        return None

    def calculate_posterior(self, X):
        posterior_dict = []
        for c in list(self.prior_dict.keys()):
            # Initialize posterior as prior
            posterior = self.prior_dict[c]['prior']
            for col_name in X.index:
                # Naive assumption (independence):
                # P(x1,x2,x3|Y) = P(x1|Y)*P(x2|Y)*P(x3|Y)
                # Posterior is product of prior and likelihoods (ignoring scaling factor)
                if(type(X[col_name]) in [int, float, np.int64, np.float]):
                    posterior *= self.calculate_gaussian_prob(X[col_name], col_name, c)
                else:
                    pass
            posterior_dict.append((c, posterior))

        return posterior_dict

    def predict(self, X):
        # For row in dataset
        self.results = [self.calculate_posterior(row) for index, row in X.iterrows()]

        return [max(prob, key=itemgetter(1))[0] for prob in self.results]

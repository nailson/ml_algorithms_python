import numpy as np
from operator import itemgetter


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
                posterior *= self.likelyhood_dict[col_name][(X[col_name], c)]
            posterior_dict.append((c, posterior))

        return posterior_dict

    def predict(self, X):
        # For row in dataset
        self.results = [self.calculate_posterior(row) for index, row in X.iterrows()]

        return [max(prob, key=itemgetter(1))[0] for prob in self.results]

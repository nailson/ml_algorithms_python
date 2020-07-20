from statistics import mode
import numpy as np


class LabeledPoint():
    vector: list
    label: str

    def __init__(self, vector, label):
        self.vector = vector
        self.label = label


class KNN():

    labeled_points_list = []

    def fit(self, X, y):
        labeled_points_list = []
        for index, row in X.iterrows():
            labeled_points_list.append(LabeledPoint(row, y.loc[index][0]))

        self.labeled_points_list = labeled_points_list

    def predict(self, X, k=3):

        def count_majority(label_list):
            return mode(label_list)

        def euclidian_distance(v, w):
            squared_diff_list = [(a-b)**2 for a, b in zip(v, w)]
            return np.sqrt(np.sum(squared_diff_list))

        predictions = []
        for index, row in X.iterrows():

            labeled_points_ordered = sorted(self.labeled_points_list,
                                            key=lambda lp: euclidian_distance(lp.vector, row.to_numpy()))
            k_nearest = [lp.label for lp in labeled_points_ordered[:k]]
            majority_class = count_majority(k_nearest)

            predictions.append(majority_class)

        return predictions

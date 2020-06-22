import numpy as np
import math


class ID3():

    def __init__(self):
        self.tree = []

    def fit(self, X, y):
        self.tree = self.buildTree(X, y, tree=None)

    def count_classes(self, label_serie):
        return label_serie.value_counts().to_dict()

    def get_entropy(self, y):
        """Calculate the Gini Impurity for a list of rows."""
        counts = self.count_classes(y)
        eps = np.finfo(float).eps
        entropy = 0

        # for each label calculate the entropy
        for lbl in counts:

            prob_of_lbl = counts[lbl] / (float(len(y)) + eps)
            entropy -= prob_of_lbl * math.log2(prob_of_lbl+eps)
        return entropy

    def max_gain(self, X, y):
        entropy_root = self.get_entropy(y)
        max_gain = 0
        split_feature = ''

        for feature in X.columns:
            entropy = 0
            for c_feature in X[feature].unique():
                split_feature_x = X.iloc[np.where(X[feature] == c_feature)]
                split_y = y[np.where(X[feature] == c_feature)[0]]
                entropy += len(split_feature_x) / len(X)*self.get_entropy(split_y)

            info_gain = entropy_root - entropy
            if(max_gain < info_gain):
                max_gain = info_gain
                split_feature = feature

        return split_feature

    def split_table(self, X, y, node, class_name):
        X1 = X[X[node] == class_name].reset_index(drop=True)
        y1 = y[np.where(X[node] == class_name)[0]].reset_index(drop=True)
        return X1, y1

    def buildTree(self, X, y, tree=None):
        # Get attribute with maximum information gain
        node = self.max_gain(X, y)

        # Get distinct value of that attribute e.g Salary is node and Low,Med and High are values
        c_features = X[node].unique()

        # Create an empty dictionary to create tree
        if tree is None:
            tree = {}
            tree[node] = {}

        for class_name in c_features:
            X_subtable, y_subtable = self.split_table(X, y, node, class_name)
            clValue, counts = np.unique(y_subtable, return_counts=True)

            # Checking if is a leaf node
            if len(counts) == 1:
                tree[node][class_name] = clValue[0]
            # Add a new node and call buildTree function recursively
            else:
                tree[node][class_name] = self.buildTree(X_subtable, y_subtable)

        return tree

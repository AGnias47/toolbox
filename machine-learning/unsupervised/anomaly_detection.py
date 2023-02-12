"""
Anomaly Detection

Resources
---------
C3_W1_Anomaly_Detection Notebook from Unsupervised Learning, Recommenders, Reinforcement Learning by Andrew Ng
"""

import numpy as np


def estimate_gaussian(X):
    m, n = X.shape
    mu = np.sum(X, axis=0) / m
    var = np.sum((X - mu) ** 2, axis=0) / m
    return mu, var


def select_epsilon(y_val, p_val):
    best_e = 0
    best_f1 = 0
    step_size = (max(p_val) - min(p_val)) / 1000
    for epsilon in np.arange(min(p_val), max(p_val), step_size):
        preds = p_val < epsilon
        true_positives = np.sum((preds == 1) & (y_val == 1))
        false_positives = np.sum((preds == 1) & (y_val == 0))
        false_negatives = np.sum((preds == 0) & (y_val == 1))
        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        f1 = (2 * precision * recall) / (precision + recall)
        if f1 > best_f1:
            best_f1 = f1
            best_e = epsilon
    return best_e, best_f1

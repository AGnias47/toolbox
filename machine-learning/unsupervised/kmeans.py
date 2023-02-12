"""
kmeans

Resources
---------
C3_W1_KMeans_Assignment Notebook from Unsupervised Learning, Recommenders, Reinforcement Learning by Andrew Ng
"""

import numpy as np


def find_closest_centroids(X, centroids):
    K = centroids.shape[0]
    assignment = np.zeros(X.shape[0], dtype=int)
    for i in range(X.shape[0]):
        distance = []
        for c in range(K):
            distance.append(np.linalg.norm(X[i] - centroids[c]))
        assignment[i] = np.argmin(distance)
    return assignment


def compute_centroids(X, centroid_assignment, K):
    m, n = X.shape
    centroids = np.zeros((K, n))
    for c in range(K):
        centroids[c] = np.mean(X[centroid_assignment == c], axis=0)
    return centroids

#!/usr/bin/env python3

"""
Used to perform k-means clustering
"""

from copy import deepcopy
import random

import matplotlib.pyplot as plt
from nltk.cluster import kmeans, cosine_distance
import numpy as np
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA


def kmeans_clustering(sample, clusters):
    """
    Performs K-Means clustering on a sample

    Parameters
    ----------
    sample: Tweet
    clusters: int

    Returns
    -------
    Collection, dict, dict, ndarray, ndarray, list
        List of cluster corresponding to sample, dict of features, dict of clusters, pca centroids, pca tweets, and
        distances of each Tweet to their closest centroid
    """
    clusterer = kmeans.KMeansClusterer(clusters, cosine_distance, rng=random.Random(42))
    vectorizer = TfidfVectorizer(lowercase=False)
    X = vectorizer.fit_transform([" ".join(x.tokenized_content) for x in sample]).todense()
    assigned_clusters = clusterer.cluster(np.asarray(X), assign_clusters=True)
    pca_centroids, pca_tweets = run_decomposition(X, clusterer)
    cluster_dict, feature_dict = generate_cluster_and_feature_dict(vectorizer, clusters, clusterer)
    distances = get_distance_from_closest_centroid(clusters, assigned_clusters, pca_centroids, pca_tweets)
    return assigned_clusters, feature_dict, cluster_dict, pca_centroids, pca_tweets, distances


def run_decomposition(X, clusterer, decomp_function=PCA):
    """
    Runs decomposition to map clusters into 2 dimensions

    Parameters
    ----------
    X: matrix
    clusterer: VectorSpaceClusterer
    decomp_function: sklearn.decomposition.* (default is PCA)

    Returns
    -------
    ndarray, ndarray
        Centroid coordinates, data coordinates
    """
    pca = decomp_function(n_components=2).fit(X)
    pca_centroids = pca.transform(clusterer.means())
    pca_tweets = pca.transform(X)
    return pca_centroids, pca_tweets


def generate_cluster_and_feature_dict(vectorizer, clusters, clusterer):
    """
    Generates dictionaries for determining the most relevant features for each cluster

    Parameters
    ----------
    vectorizer: CountVectorizer
    clusters: int
    clusterer: VectorSpaceClusterer

    Returns
    -------
    dict, dict
        Dict mapping clusters to relevant features, dict mapping matrix indicies to specific feature
    """
    feature_dict = dict()
    for i, feature in np.ndenumerate(vectorizer.get_feature_names_out()):
        feature_dict[i] = feature
    cluster_dict = dict()
    for i in range(clusters):
        cluster_dict[i] = dict()
        for j, val in np.ndenumerate(clusterer.means()[i]):
            cluster_dict[i][j] = val
        cluster_dict[i] = dict(sorted(cluster_dict[i].items(), key=lambda item: abs(item[1]), reverse=True))
    return cluster_dict, feature_dict


def get_distance_from_closest_centroid(k, clusters, pca_centroids, pca_tweets, distance_function=cosine_distance):
    """
    Gets the distance from a data point to its closest centroid

    Parameters
    ----------
    k: int
    clusters: Collection
        List of cluster corresponding to each data point
    pca_centroids: ndarray
    pca_tweets: ndarray
    distance_function: function
        One of cosine_distance, euclidean_distance

    Returns
    -------
    list
        List of Tweet distances to nearest cluster corresponding to each Tweet
    """
    distances = list()
    for i in range(k):
        for j in range(pca_tweets.shape[0]):
            if int(clusters[j]) == i:
                distances.append(round(distance_function(pca_centroids[i], pca_tweets[j]), 5))
    return distances


def write_relevant_features_to_file(fname, clusters, cluster_dict, feature_dict, feature_count=5):
    """
    Writes the features with the highest weight in each cluster to a file

    Parameters
    ----------
    fname: str
    clusters: int
        Number of clusters
    cluster_dict: dict
        dict of dicts. for each cluster, maps feature index to weight
    feature_dict: dict
        Maps index to word
    feature_count: int
        Number of features to report

    Returns
    -------
    None
    """
    with open(fname, "w") as F:
        for i in range(clusters):
            j = 0
            for k, v in cluster_dict[i].items():
                F.write(f"{feature_dict[k]} ({round(v, 3)})")
                j += 1
                if j >= feature_count:
                    F.write("\n")
                    break
                F.write(", ")
    return None


def run_kmeans_and_plot_data(sample, k, colormap="viridis"):
    """
    Runs k-means clustering on a dataset and plots the data

    Parameters
    ----------
    sample: Collection
    k: int
        Number of clusters
    colormap: str (default is viridis)
        See https://matplotlib.org/stable/tutorials/colors/colormaps.html for options

    Returns
    -------
    Collection, dict, dict, ndarray, ndarray, Collection
        List of cluster corresponding to sample, dict of features, dict of clusters, pca centroids, pca tweets, and
        distances of each Tweet to their closest centroid
    """
    clusters, feature_dict, cluster_dict, pca_centroids, pca_data, distances = kmeans_clustering(sample, k)
    scatterplot = sns.scatterplot(
        x=pca_data[:, 0], y=pca_data[:, 1], hue=clusters, s=5, alpha=0.7, palette=colormap
    )
    sns.scatterplot(
        x=pca_centroids[:, 0],
        y=pca_centroids[:, 1],
        hue=range(k),
        s=25,
        ax=scatterplot,
        palette=colormap,
        legend=False,
    )
    for i in range(k):
        content = "("
        j = 0
        for key, v in cluster_dict[i].items():
            if j > 0:
                content += ", "
            content += feature_dict[key]
            j += 1
            if j >= 3:
                content += ")"
                break
        plt.text(s=content, x=pca_centroids[i, 0], y=pca_centroids[i, 1], fontsize=7)
    plt.show()
    return clusters, feature_dict, cluster_dict, pca_centroids, pca_data, distances

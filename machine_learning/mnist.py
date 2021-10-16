#!/usr/bin/env python3

import random

import mnist
import seaborn as sns
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

DEBUG = True

"""
Example of using Logistic Regression with the MNIST data set
"""

def reshape(data):
    """
    From mnist package data readme

    Parameters
    ----------
    data - data to reshape

    Returns
    -------
    Reshaped data
    """
    return data.reshape(data.shape[0], data.shape[1] * data.shape[2])


def get_training_data():
    """
    From mnist package readme

    Returns
    -------
    Training data
    """
    return reshape(mnist.train_images()), mnist.train_labels()


def get_testing_data():
    """
    From mnist package readme

    Returns
    -------
    Testing data
    """
    return reshape(mnist.test_images()), mnist.test_labels()


if __name__ == "__main__":
    training_images, training_labels = get_training_data()
    if DEBUG:
        random_index = random.randint(0, len(training_images))
        image = training_images[random_index]
        label = training_labels[random_index]
        sns.heatmap(image.reshape(28, 28))
        plt.xlabel(label)
        plt.show()
    algo = LogisticRegression()
    algo.fit(training_images, training_labels)
    test_images, test_labels = get_testing_data()
    print(algo.score(test_images, test_labels))


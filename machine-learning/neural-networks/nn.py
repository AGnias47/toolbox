#!/usr/bin/env python3

"""
Script implementation of C2_W1_Assignment Notebook from Advanced Learning Algorithms course by Andrew Ng
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def keras_model():
    model = Sequential(
        [
            tf.keras.Input(shape=(400,)),  # specify input size
            Dense(units=25, activation="sigmoid"),
            Dense(units=15, activation="sigmoid"),
            Dense(units=1, activation="sigmoid"),
        ],
        name="my_model",
    )
    [layer1, layer2, layer3] = model.layers
    W1, b1 = layer1.get_weights()
    W2, b2 = layer2.get_weights()
    W3, b3 = layer3.get_weights()
    print(f"W1 shape = {W1.shape}, b1 shape = {b1.shape}")
    print(f"W2 shape = {W2.shape}, b2 shape = {b2.shape}")
    print(f"W3 shape = {W3.shape}, b3 shape = {b3.shape}")


def sigmoid(z):
    """
    Implementation of the sigmoid function

    Parameters
    ----------
    z: float

    Returns
    -------
    float
    """
    return 1 / (1 + np.exp(-z))


def numpy_dense_layer(a_input, W, b):
    z = np.matmul(a_input, W) + b
    return sigmoid(z)

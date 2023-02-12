#!/usr/bin/env python3

"""
Script implementation of  Notebook from Advanced Learning Algorithms course by Andrew Ng

Resources
---------
Notebooks from Advanced Learning Algorithms by Andrew Ng
* C2_W1_Assignment
* C2_W2_Assignment

"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def keras_model():
    model = Sequential(
        [
            tf.keras.Input(shape=(400,)),  # specify input size
            Dense(units=25, activation="relu", name="L1"),
            Dense(units=15, activation="relu", name="L2"),
            Dense(units=10, activation="relu", name="L3"),
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
    model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        optimizer=tf.keras.optimizers.Adam(0.01),
    )
    return model


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


def softmax(z):
    N = len(z)
    a = np.zeros(N)
    ez_sum = 0
    for k in range(N):
        ez_sum += np.exp(z[k])
    for j in range(N):
        a[j] = np.exp(z[j]) / ez_sum
    return a


def mse(y, y_hat):
    m = len(y)
    err = 0
    for i in range(m):
        err += (y_hat[i] - y[i]) ** 2
    return err / (2 * m)



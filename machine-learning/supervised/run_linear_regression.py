#!/usr/bin/env python3

"""
Linear Regression Model
Resources
---------
Notebooks from Supervised Machine Learning: Regression and Classification by Andrew Ng
* C1_W1_Lab04_Gradient_Descent_Soln
* C1_W2_Lab02_Multiple_Variable_Soln
"""


import matplotlib.pyplot as plt
import numpy as np

from gradient_descent.gradient_descent import gradient_descent
from linear_regression import single_variable, multiple_variable


def single_variable_gradient_descent(X, Y, w, b):
    w, b, j_hist = gradient_descent(
        X,
        Y,
        w,
        b,
        single_variable.gradients,
        single_variable.cost_function,
        1000,
        0.001,
        None,
        True,
    )
    print("Ideal weights")
    print("-------------")
    print(f"w: {w}")
    print(f"b: {b}")
    print("Predictions")
    print("-----------")
    for x in range(1, 6):
        print(f"X: {x}")
        print(f"Y: {single_variable.model(x, w, b)}")
    return j_hist


def multiple_variable_gradient_descent(X, Y, w, b):
    w, b, j_hist = gradient_descent(
        X,
        Y,
        w,
        b,
        multiple_variable.gradients,
        multiple_variable.cost_function,
        1000,
        1e-7,
        None,
        True,
    )
    print("Ideal weights")
    print("-------------")
    print(f"w: {w}")
    print(f"b: {b}")
    print("Predictions")
    print("-----------")
    for i in range(X.shape[0]):
        print(f"X: {X[i]}")
        print(f"Y: {multiple_variable.model(X[i], w, b)}")
    return j_hist


if __name__ == "__main__":
    X = np.array([1, 3, 5])
    Y = np.array([700, 900, 1450])
    w = 0
    b = 0
    j_hist_single = single_variable_gradient_descent(X, Y, w, b)
    # Each array represents X values from a training example
    X = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
    Y = np.array([460, 232, 178])

    # Training matrix will have dimensions m x n, where M is the number of training examples and n is the number of
    #   features
    w = np.array([0, 0, 0, 0])
    b = 0
    j_hist_multiple = multiple_variable_gradient_descent(X, Y, w, b)

    fig, ax = plt.subplots(1, 2, figsize=(16, 5))
    ax[0].plot(j_hist_single)
    ax[0].set_xlabel("Iteration")
    ax[0].set_ylabel("Cost")
    ax[1].plot(j_hist_multiple)
    ax[1].set_xlabel("Iteration")
    ax[1].set_ylabel("Cost")
    plt.show()

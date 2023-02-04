#!/usr/bin/env python3

"""
Linear Regression Model

Resources
---------
C1_W1_Lab04_Gradient_Descent_Soln notebook from Supervised Machine Learning: Regression and Classification by Andrew Ng
"""

import numpy as np

X = np.array([1, 3, 5])
Y = np.array([700, 900, 1450])
M = len(X)
A = 0.001
GD_ITER = 1000
DEBUG = True


def model(x, w, b):
    """
    Linear Regression Model

    Parameters
    ----------
    x: float
    w: float
    b: float

    Returns
    -------
    float
    """
    return w * x + b


def cost_function(w, b):
    """
    Squared error cost function

    Parameters
    ----------
    w: float
    b: float

    Returns
    -------
    float
    """
    total_error = 0.0
    for i in range(M):
        total_error += (model(X[i], w, b) - Y[i]) ** 2
    return (1 / (2 * M)) * total_error


def gradient_descent(w=0, b=0):
    """
    Gradient descent function. Prints and stores debug info if true

    Parameters
    ----------
    w: float
    b: float

    Returns
    -------
    float, float, list, list
    """
    j = list()
    p = list()
    for i in range(GD_ITER):
        dj_dw, dj_db = gradients(w, b)
        w -= A * dj_dw
        b -= A * dj_db
        if DEBUG and i < 100_000:
            cost = cost_function(w, b)
            if i % 100 == 0:
                print(f"Cost: {cost}")
            j.append(cost)
            p.append([w, b])
    return w, b, j, p


def gradients(w, b):
    """
    Computes the partial derivatives of w and b with respect to the cost function

    Parameters
    ----------
    w: float
    b: float

    Returns
    -------
    float
    """
    dj_dw = 0.0
    dj_db = 0.0
    for i in range(M):
        model_result = model(X[i], w, b)
        dj_dw += (model_result - Y[i]) * X[i]
        dj_db += model_result - Y[i]
    oom = 1 / M
    return oom * dj_dw, oom * dj_db


if __name__ == "__main__":
    w, b, j_hist, weights_hist = gradient_descent()
    print("Ideal weights")
    print("-------------")
    print(f"w: {w}")
    print(f"b: {b}")
    print("Predictions")
    print("-----------")
    for x in range(1, 6):
        print(f"X: {x}")
        print(f"Y: {model(x, w, b)}")
    if DEBUG:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(1, 1, figsize=(8, 5))
        ax.plot(j_hist)
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Cost")
        plt.show()

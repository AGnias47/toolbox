#!/usr/bin/env python3

X = [1, 18, 27]
Y = [1, 3, 5]
M = len(X)


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
    return w*x + b


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
        total_error += (model(X[i], w, b) - Y[i])**2
    return (1 / (2*M)) * total_error




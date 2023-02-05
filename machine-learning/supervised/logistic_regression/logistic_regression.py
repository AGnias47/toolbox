import numpy as np


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


def model(x, w, b):
    """
    Model for logistic regression
    Parameters
    ----------
    x: np.array
    w: np.array
    b: float

    Returns
    -------
    float
    """
    z = np.dot(x, w) + b
    return sigmoid(z)


def gradients(X, Y, w, b):
    """
    Computes the partial derivatives of w and b with respect to the cost function

    Note that this is the same implementation as the linear regression function for multiple variables, just with a
    different model

    Parameters
    ----------
    X: np.array
    Y: np.array
    w: np.array
    b: float

    Returns
    -------
    np.array, float
    """
    m, n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.0
    for i in range(m):
        model_result = model(X[i], w, b)
        for j in range(n):
            dj_dw[j] += (model_result - Y[i]) * X[i, j]
        dj_db += model_result - Y[i]
    return dj_dw / m, dj_db / m


def compute_cost(X, Y, w, b, lam=None):
    """
    Logistic regression cost function

    Parameters
    ----------
    X: np.array
    Y: np.array
    w: np.array
    b: float
    lam: float

    Returns
    -------
    float
    """
    total_error = 0.0
    m, n = X.shape
    for i in range(m):
        model_result = model(X[i], w, b)
        total_error += -Y[i] * np.log(model_result) - (1 - Y[i]) * np.log(
            1 - model_result
        )
    total_error = total_error / m
    if lam:
        regularized_cost = 0.0
        for i in range(n):
            regularized_cost += w[i] ** 2
        regularized_cost = (lam / (2 * m)) * regularized_cost
        total_error += regularized_cost
    return total_error

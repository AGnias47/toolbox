import numpy as np


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
    return np.dot(x, w) + b


def gradients(X, Y, w, b):
    """
    Computes the partial derivatives of w and b with respect to the cost function

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


def cost_function(X, Y, w, b):
    """
    Squared error cost function

    Parameters
    ----------
    X: np.array
    Y: np.array
    w: float
    b: float

    Returns
    -------
    float
    """
    total_error = 0.0
    M = X.shape[0]
    for i in range(M):
        total_error += (model(X[i], w, b) - Y[i]) ** 2
    return (1 / (2 * M)) * total_error

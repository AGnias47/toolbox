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


def gradients(X, Y, w, b):
    """
    Computes the partial derivatives of w and b with respect to the cost function

    Parameters
    ----------
    X: np.array
    Y: np.array
    w: float
    b: float

    Returns
    -------
    float, float
    """
    dj_dw = 0.0
    dj_db = 0.0
    M = len(X)
    for i in range(M):
        model_result = model(X[i], w, b)
        dj_dw += (model_result - Y[i]) * X[i]
        dj_db += model_result - Y[i]
    return dj_dw / M, dj_db / M


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
    M = len(X)
    for i in range(M):
        total_error += (model(X[i], w, b) - Y[i]) ** 2
    return (1 / (2 * M)) * total_error

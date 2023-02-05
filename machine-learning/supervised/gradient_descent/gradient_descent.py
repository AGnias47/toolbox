def gradient_descent(
    X,
    Y,
    w,
    b,
    gradient_function,
    cost_function,
    gd_iter,
    alpha,
    lam=None,
    debug=False,
):
    """
    Gradient descent function. Prints and stores debug info if true

    Parameters
    ----------
    X: np.array
    Y: np.array
    w: float
    b: float
    gradient_function: function
    cost_function: function
    gd_iter: int
    alpha: float
    lam: float (default is None)
    debug: bool (default is False)

    Returns
    -------
    float, float, list, list
    """
    j = list()
    m = X.shape[0]
    for i in range(gd_iter):
        dj_dw, dj_db = gradient_function(X, Y, w, b)
        if lam:
            w = w - alpha * (dj_dw + (lam/m)*w)
        else:
            w = w - alpha * dj_dw
        b = b - alpha * dj_db
        if debug and i < 100_000:
            cost = cost_function(X, Y, w, b, lam)
            if i % 100 == 0:
                print(f"Cost: {cost}")
            j.append(cost)
    return w, b, j

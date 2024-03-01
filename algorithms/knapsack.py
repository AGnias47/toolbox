#!/usr/bin/env python

"""
Sources
* p. 269 of Algorithm Design by Jon Kleinberg and Éva Tardos
* https://chat.openai.com/c/8824a98d-5cc1-4a24-8df9-04f527ca3361
"""


def subset_sum(n, W, weights, M=None):
    if not M:
        M = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if w < weights[i - 1]:
                M[i][w] = M[i - 1][w]
            else:
                M[i][w] = max(
                    M[i - 1][w], weights[i - 1] + M[i - 1][w - weights[i - 1]]
                )
    return M[n][W]


if __name__ == "__main__":
    n = 3
    W = 6
    weights = [2, 2, 3]
    print(subset_sum(n, W, weights))

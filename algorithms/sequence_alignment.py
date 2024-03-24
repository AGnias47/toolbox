#!/usr/bin/env python

"""
Sequence Alignment algorithm from p. 282 of Algorithm Design by Jon Kleinberg and Éva
Tardos. Also utilized https://chat.openai.com/share/861f99e2-830a-48f8-a40a-f153beff33a9
as a resource for implementation.
"""

DELTA = 1


def alpha(a, b):
    if a == b:
        return 0
    else:
        return 1


def alignment(X, Y, A=None):
    m = len(X) + 1
    n = len(Y) + 1
    if not A:
        A = [[0] * (n) for _ in range(m)]
    for i in range(m):
        A[i][0] = i * DELTA
    for j in range(n):
        A[0][j] = j * DELTA
    for j in range(1, n):
        for i in range(1, m):
            case_1 = alpha(X[i], Y[j]) + A[i - 1][j - 1]
            case_2 = DELTA + A[i - 1][j]
            case_3 = DELTA + A[i][j - 1]
            return min(case_1, case_2, case_3)
    return A[m][n]


if __name__ == "__main__":
    string_pairs = [("coffee", "coffee"), ("ACTG", "AATG")]
    for pair in string_pairs:
        result = alignment(pair[0], pair[1])
        print(f"Pair: {pair[0]}, {pair[1]}")
        print(f"Result: {result}")

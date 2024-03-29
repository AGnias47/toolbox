#!/usr/bin/env python

"""
Sequence Alignment algorithm from p. 282 of Algorithm Design by Jon Kleinberg and Éva
Tardos. Also utilized https://chat.openai.com/share/861f99e2-830a-48f8-a40a-f153beff33a9
as a resource for implementation.
"""


def alpha(a, b):
    if a == b:
        return 0
    else:
        # If both are vowels or consonants; doesn't matter which, as long as they match
        if vowel(a) == vowel(b):
            return 1
        else:
            return 3


def delta():
    return 2


def vowel(a):
    if a.upper() in "AEIOU":
        return True
    return False


def alignment(X, Y, A=None):
    m = len(X)
    n = len(Y)
    if not A:
        A = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        A[i][0] = i * delta()
    for j in range(n + 1):
        A[0][j] = j * delta()
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                case_1 = alpha(X[i - 1], Y[j - 1]) + A[i - 1][j - 1]
                case_2 = delta() + A[i - 1][j]
                case_3 = delta() + A[i][j - 1]
                A[i][j] = min(case_1, case_2, case_3)
    return A[m][n]


if __name__ == "__main__":
    string_pairs = [("coffee", "coffee"), ("ACTG", "AATG"), ("GENIE", "GAME")]
    for pair in string_pairs:
        result = alignment(pair[0], pair[1])
        print(f"Pair: {pair[0]}, {pair[1]}")
        print(f"Result: {result}")

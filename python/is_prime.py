#!/usr/bin/env python3

import sys
from random import randint


def fermat(n, iterations=1):
    """
    Uses Fermat's probabilistic algorithm to determine if a number is prime

    Parameters
    ---------
    n: int
        Number to check
    iterations: int
        How many checks to run on Fermat's theorem

    Returns
    -------
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    results = list()
    for _ in range(iterations):
        results.append((randint(1, n - 2) ** (n - 1)) % n == 1)
    return all(results)


if __name__ == "__main__":
    assert fermat(1163) == True
    assert fermat(24601) == False
    assert fermat(7879, 5) == True
    assert fermat(63, 7) == False
    assert fermat(12959) == True
    try:
        print(fermat(int(sys.argv[1])))
    except IndexError:
        pass

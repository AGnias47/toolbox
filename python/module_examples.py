#!/usr/bin/env python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

import tqdm
import functools


def tqdm_usage():
    """Example of using tqdm progress bar"""
    for i in tqdm.tqdm(range(9999999)):
        pass


@functools.lru_cache
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    tqdm_usage()
    print(fibonacci(100))

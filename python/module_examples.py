#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

import tqdm


def tqdm_usage():
    """Example of using tqdm progress bar"""
    for i in tqdm.tqdm(range(9999999)):
        a = 1


if __name__ == "__main__":
    tqdm_usage()

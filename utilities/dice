#!/usr/bin/env python3
#
#   A. Gnias
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.7.5
#   Vim 8.1

import random
import sys


def roll(di, sides):
    total = list()
    for r in range(di):
        total.append(random.randint(1, sides))
    return total, sum(total)


if __name__ == "__main__":
    try:
        print(roll(int(sys.argv[1]), int(sys.argv[2])))
    except IndexError:
        print("Provide dice to roll and number of sides as positional arguments")
    except ValueError:
        print("Dice to roll and sides must be integers")

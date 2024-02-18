#!/usr/bin/env python3

"""
From p.124 of Algorithm Design by J. Kleinberg and E. Tardos:
Sort the intervals by their start times, breaking ties arbitrarily
Let I1, I2,...,In In denote the intervals in this order
For j = 1, 2, 3, . . . , n
    For each interval Ii that precedes Ij in sorted order and overlaps it
        Exclude the label of Ii from consideration for Ij
    Endfor
    If there is any label from {1, 2, . . . , d} that has not been excluded then
        Assign a nonexcluded label to Ij
    Else
        Leave Ij unlabeled
    Endif
Endfor
"""

from typing import List, Set


class Request:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.label = None

    def __repr__(self):
        return f"Request: start {self.start}, end {self.end}, label {self.label}"

    def __lt__(self, other):
        return self.start < other.start

    @property
    def duration(self):
        return self.end - self.start

    def compatible(self, r):
        return self.end <= r.start or self.start >= r.end


def schedule(R: Set[Request]) -> (List[Request], int):
    """
    Interval partitioning algorithm using greedy approach.


    Parameters
    ----------
    R: Set
        Set of requests

    Returns
    -------
    List, int
        List of accepted requests, number of partitions used
    """
    A = list()
    I = sorted(list(R))
    n = len(I)
    d = 1
    for j in range(n):
        exclusions = set()
        for k in range(j, -1, -1):
            if j == k:
                continue
            if not I[j].compatible(I[k]):
                exclusions.add(I[k].label)
        for i in range(1, d+1):
            if i not in exclusions:
                I[j].label = i
                break
        if I[j].label is None:
            d += 1
            I[j].label = d
        A.append(I[j])
    return A, d


if __name__ == "__main__":
    r1 = Request(1, 10)
    r2 = Request(3, 5)
    r3 = Request(6, 8)
    r4 = Request(20, 30)
    R = {r1, r2, r3, r4}
    print("Requests")
    print(*sorted(list(R)), sep="\n")
    A, d = schedule(R)
    print("Scheduled Requests")
    print(*A, sep="\n")
    print(f"Number of partitions: {d}")

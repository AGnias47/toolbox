#!/usr/bin/env python3

"""
From p.118 of Algorithm Design by J. Kleinberg and E. Tardos:

Initially let R be the set of all requests, and let A be empty
While R is not yet empty
    Choose a request i∈R that has the smallest finishing time
    Add request i to A
    Delete all requests from R that are not compatible with request i
EndWhile
Return the set A as the set of accepted requests
"""

from typing import List, Set


class Request:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Request: start {self.start}, end {self.end}"

    def __lt__(self, other):
        return self.end < other.end

    @property
    def duration(self):
        return end - start

    def compatible(self, r):
        return self.end <= r.start or self.start >= r.end


def schedule(R: Set) -> List:
    A = list()
    requests = sorted(list(R))
    for r in requests:
        if not A or r.compatible(A[-1]):
            A.append(r)
    return A


if __name__ == "__main__":
    r1 = Request(1, 10)
    r2 = Request(3, 5)
    r3 = Request(6, 8)
    R = {r1, r2, r3}
    print("Requests")
    print(*sorted(list(R)), sep="\n")
    A = schedule(R)
    print("Scheduled Requests")
    print(*A, sep="\n")

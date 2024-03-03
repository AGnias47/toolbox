#!/usr/bin/env python3


S = [1,2,2,3,3,3,4,5]

def equivalent(a, b):
    return a == b

def create_set(S):
    if len(S) == 1:
        return True
    sets = []
    for i in range(S):

"""
Among n cards, is there a set > n/2 where all are equivalent? Solve in nlog(n) 
equivalence checks
"""
#!/usr/bin/env python

"""
Meant to find the longest path in a directed, ordered graph. This is a very simple graph
implementation. Each node is represented by a list. The first element of the list is the
node's value, and the rest of the elements are the nodes that the current node points
to. The graph is represented by a list of nodes. The first element of the list is a
sentinel value, and the rest of the elements are the nodes in the graph. M is the
memoization array.
"""

v1 = [1, 2, 3]
v2 = [2, 5]
v3 = [3, 4]
v4 = [4, 5]
v5 = [5]
SENTINEL = 0
available_nodes = [SENTINEL, v1, v2, v3, v4, v5]
M = [None] * len(available_nodes)


def longest_path_incorrect(v):
    w = v
    length = 0
    while len(w) > 1:
        v_min = min(w[1:])
        w = available_nodes[v_min]
        length += 1
    return length


def longest_path(v):
    if not M[v[0]]:
        max_edge = 0
        for edge in v[1:]:
            edge_path = longest_path(available_nodes[edge]) + 1
            if edge_path > max_edge:
                max_edge = edge_path
        M[v[0]] = max_edge
    return M[v[0]]


print(longest_path_incorrect(v1))
print(longest_path(v1))

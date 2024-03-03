#!/usr/bin/env python

"""
Meant to find the longest path in a directed, ordered graph. This is a very simple graph
implementation. Each node is represented by a list. The first element of the list is the
node's value, and the rest of the elements are the nodes that the current node points
to. The graph is represented by a list of nodes. The first element of the list is a
sentinel value, and the rest of the elements are the nodes in the graph. M is the
memoization array.
"""

SENTINEL = 0


def longest_path(v):
    if not M[v[0]]:
        max_edge = 0
        for edge in v[1:]:
            edge_path = longest_path(available_nodes[edge]) + 1
            if edge_path > max_edge:
                max_edge = edge_path
        M[v[0]] = max_edge
    return M[v[0]]


if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [2, 5]
    v3 = [3, 4]
    v4 = [4, 5]
    v5 = [5]
    available_nodes = [SENTINEL, v1, v2, v3, v4, v5]
    M = [None] * len(available_nodes)
    print(longest_path(v1))
    print("-----")
    v1 = [1, 2, 3, 4]
    v2 = [2, 5, 7]
    v3 = [3, 5]
    v4 = [4, 6]
    v5 = [5, 6]
    v6 = [6, 7]
    v7 = [7]
    available_nodes = [SENTINEL, v1, v2, v3, v4, v5, v6, v7]
    M = [None] * len(available_nodes)
    print(longest_path(v1))

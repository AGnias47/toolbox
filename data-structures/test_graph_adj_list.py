#!/usr/bin/env python3

from graph_adj_list import Graph, Color


def test_initialization():
    graph = Graph("resources/graph1.txt")
    assert 8 == graph.size
    assert 8 == len(graph.vertices)
    check_adjacency_list([2, 5], graph.adjacency_lists[1])
    check_adjacency_list([1, 6], graph.adjacency_lists[2])
    check_adjacency_list([4, 6, 7], graph.adjacency_lists[3])
    check_adjacency_list([3, 7, 8], graph.adjacency_lists[4])
    check_adjacency_list([1], graph.adjacency_lists[5])
    check_adjacency_list([2, 3, 7], graph.adjacency_lists[6])
    check_adjacency_list([3, 4, 6, 8], graph.adjacency_lists[7])
    check_adjacency_list([4, 7], graph.adjacency_lists[8])


def check_adjacency_list(expected_vertices, adj_list):
    actual_vertices = list()
    traverser = adj_list.node
    while traverser:
        actual_vertices.append(traverser.vertex)
        traverser = traverser.node
    expected_vertices.sort()
    actual_vertices.sort()
    assert expected_vertices == actual_vertices


def test_BFS():
    graph = Graph("resources/graph1.txt")
    order, color, predecessor, distance = graph.BFS(2)
    assert [2, 1, 6, 5, 3, 7, 4, 8] == order
    for _, c in color.items():
        assert c == Color.BLACK


def test_DFS():
    graph = Graph("resources/graph2.txt")
    order, color, predecessor, discovered, finished = graph.DFS()
    assert [4, 5, 2, 1, 6, 3] == order
    for _, c in color.items():
        assert c == Color.BLACK


if __name__ == "__main__":
    test_initialization()
    test_BFS()
    test_DFS()

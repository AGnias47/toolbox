#!/usr/bin/env python3

from math import inf
from enum import Enum
from collections import deque
from operator import attrgetter

"""
Graph with adjacency matrix representation
"""


def create_matrix(size):
    """Initialize a matrix as a Python list of lists.
    Indices of the matrix can then be called as m[row][column]

    Args:
        size (int): Number of vertices in the graph

    Returns:
        list(list())

    Time Complexity: T(V^2)
    """
    # m^2 matrix
    return [[0 for _x in range(size)] for _y in range(size)]


class Color(Enum):
    """
    Enum for Node colors used in BFS / DFS
    """

    WHITE = 0
    GREY = 1
    BLACK = 2


class Edge:
    def __init__(self, u, v, w):
        """
        Edge representation in a graph
        Args:
            u: vertex 1
            v: vertex 2
            w: weight
        """
        self.u = u
        self.v = v
        self.w = w

    def __eq__(self, o):
        return self.w == o.w and (self.u == o.u and self.v == o.v) or (self.u == o.v and self.v == o.u)

    def __add__(self, other):
        return self.w + other.w

    def __str__(self):
        return f"{self.u}->{self.v}, {self.w}"

    def __hash__(self):
        return id(self)


class PrimVertex:
    def __init__(self, v, k, p):
        """
        Extended vertex representation for Prim's Algorithm
        Args:
            v: vertex
            k: weight
            p: predecessor
        """
        self.vertex = v
        self.key = k
        self.pred = p

    def __eq__(self, o):
        return self.vertex == o.vertex and self.key == o.key and self.pred == o.pred

    def __add__(self, other):
        return self.key + other.key

    def __str__(self):
        return f"{self.vertex} ({self.key})"

    def __hash__(self):
        return id(self)


class SetHandler:
    def __init__(self):
        """
        Used to handle set operations in Kruskal's algorithm
        """
        self.handler = list()

    def add(self, s):
        """
        Add a set
        Args:
            s: set

        Returns: None
        """
        self.handler.append(s)

    def find_set(self, v):
        """
        Searches for a set containing v. If it exists, returns the index in the handler where it is located.
        If it does not exist, returns -1
        Args:
            v: int

        Returns: int
        """
        for i, s in enumerate(self.handler):
            if v in s:
                return i
        return -1

    def union(self, e):
        """
        Combines the sets containing each vertex in a Graph's edge.
        Args:
            e: Edge

        Returns: None
        """
        u_index, v_index = None, None
        u_found, v_found = False, False
        for i, s in enumerate(self.handler):
            if e.u in s:
                u_index = i
                u_found = True
            if e.v in s:
                v_index = i
                v_found = True
            if u_found and v_found:
                break
        if not (u_found and v_found):
            RuntimeError("Something went wrong")
        self.handler[u_index] = self.handler[u_index].union(self.handler[v_index])
        self.handler.pop(v_index)


class Graph:
    def __init__(self, graph_file):
        """
        Create a Graph from a text file of the format:
            u_1->v_1,weight->v_2,weight->v_n,weight
            u_2->v_1,weight->v_2,weight->v_n,weight
            u_n->v_1-,weight>v_2,weight->v_n,weight

        Args:
            graph_file (string): Path to file

        Time Complexity: T(V^2)
        """
        self.size = 0
        with open(graph_file, "r") as F:
            for _ in F:
                self.size += 1
        self.vertices = set()
        self.adjacency_matrix = create_matrix(self.size + 1)
        self.edges = set()
        with open(graph_file, "r") as F:
            for line in F:
                tokens = line.split("->")
                vertex = int(tokens[0].strip())
                self.vertices.add(vertex)
                is_vertex = True
                for token in tokens:
                    if is_vertex:
                        is_vertex = False
                    else:
                        dest, weight = token.strip().split(",")
                        self.adjacency_matrix[vertex][int(dest)] = int(weight)
                        self.edges.add(Edge(vertex, int(dest), int(weight)))

    def BFS(self, s):
        """Perform a Breadth-first search on the graph starting at a specified vertex

        Args:
            s (int): Vertex to start at

        Returns:
            list, dict, dict, dict: list displaying order items are found in, and dicts of
            predecessors, distance, and colors, respectively

        Time Complexity: T(V+E)
        """
        color = dict()
        predecessor = dict()
        distance = dict()
        order = list()
        for vertex in self.vertices:
            color[vertex] = Color.WHITE
            distance[vertex] = -1
            predecessor[vertex] = None
        color[s] = Color.GREY
        distance[s] = 0
        predecessor[s] = None
        Q = deque()
        Q.append(s)
        while len(Q) > 0:
            u = Q.popleft()
            for v in range(1, self.size + 1):
                if self.adjacency_matrix[u][v] == 1:
                    if color[v] == Color.WHITE:
                        color[v] = Color.GREY
                        distance[v] = distance[u] + 1
                        predecessor[v] = u
                        Q.append(v)
            color[u] = Color.BLACK
            order.append(u)
        return order, color, predecessor, distance

    def DFS(self, vertices=None):
        """
        Performs a Depth-first search on the Graph

        Args:
            vertices (list, optional): List of vertices to include in DFS. If none, all vertices
            in the graph will be included.

        Returns:
            list, dict, dict, dict: list displaying order items are found in, and dicts of
            colors, predecessors, discovered vertices, and finished vertices, respectively

        Time Complexity: T(V+E)
        """
        if vertices is None:
            vertices = self.vertices
        order = list()
        color = dict()
        predecessor = dict()
        discovered = dict()
        finished = dict()
        for u in self.vertices:
            color[u] = Color.WHITE
            predecessor[u] = None
        time = 0
        for u in vertices:
            if color[u] == Color.WHITE:
                self.DFS_visit(u, time, order, color, predecessor, discovered, finished)
        return order, color, predecessor, discovered, finished

    def DFS_visit(self, u, time, order, color, predecessor, discovered, finished):
        """
        Helper function to DFS used to visit reachable vertices
        Args:
            u: vertex
            time: time variable that vertex is found
            order: order list for discovered vertices
            color: color dict for vertices
            predecessor: predecessor dict for vertices
            discovered: discovered vertices
            finished: finished vertices

        Returns:
            None

        Time Complexity: T(V+E)
        """
        color[u] = Color.GREY
        time += 1
        discovered[u] = time
        for v in range(1, self.size + 1):
            if self.adjacency_matrix[u][v] == 1:
                if color[v] == Color.WHITE:
                    predecessor[v] = u
                    self.DFS_visit(v, time, order, color, predecessor, discovered, finished)
        color[u] = Color.BLACK
        order.append(u)
        time += 1
        finished[u] = time
        return None

    def transpose(self):
        """
        Transpose the adjacency matrix of the graph

        Time Complexity: T(V^2)
        """
        for i in range(1, self.size + 1):
            for j in range(i, self.size + 1):
                self.adjacency_matrix[i][j], self.adjacency_matrix[j][i] = (
                    self.adjacency_matrix[j][i],
                    self.adjacency_matrix[i][j],
                )

    def mst_kruskal(self):
        """
        Creates an MST using Kruskal's Algorithm

        Returns: list
            List of Edge objects in the MST
        """
        A = list()
        S = SetHandler()
        for v in self.vertices:
            S.add({v})
        edges = sorted(self.edges, key=attrgetter("w"))
        for e in edges:
            if S.find_set(e.u) != S.find_set(e.v):
                A.append(e)
                S.union(e)
        return A

    def mst_prim(self):
        """
        Creates an MST using Prim's Algorithm

        Returns: list
            List of PrimVertex objects in order of which they are added
        """
        vertices = dict()
        Q = list()
        A = list()
        for v in self.vertices:
            v_struct = PrimVertex(v, inf, None)
            Q.append(v_struct)
            vertices[v] = v_struct
        Q.sort(key=attrgetter("key"))
        while Q:
            u = Q.pop(0)
            A.append(u)
            vertices.pop(u.vertex)
            for i, v in enumerate(self.adjacency_matrix[u.vertex]):
                if v > 0 and i in vertices:
                    v = vertices[i]
                    weight = next(filter(lambda x: x.u == u.vertex and x.v == v.vertex, self.edges)).w
                    if weight < v.key:
                        v.pred = u
                        v.key = weight
            Q.sort(key=attrgetter("key"))
        A[0].key = 0
        return A


if __name__ == "__main__":
    graph1 = Graph("resources/graph1_weighted.txt")
    A = graph1.mst_kruskal()
    print(*A, sep="\n")
    total = 0
    for e in A:
        total += e.w
    print(total)
    P = graph1.mst_prim()
    print(*P, sep="->")
    total = 0
    for v in P:
        total += v.key
    print(total)

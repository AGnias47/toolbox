#!/usr/bin/env python3

from enum import Enum
from collections import deque


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


class Graph:
    def __init__(self, graph_file):
        self.size = 0
        self.vertices = set()
        self.adjacency_lists = dict()
        with open(graph_file, "r") as F:
            for line in F:
                tokens = line.split("->")
                vertex = int(tokens[0].strip())
                self.size += 1
                self.vertices.add(vertex)
                is_vertex = True
                for token in tokens:
                    if is_vertex:
                        self.adjacency_lists[vertex] = AdjNode(None)
                        is_vertex = False
                    else:
                        traverser = self.adjacency_lists[vertex]
                        while traverser.node is not None:
                            traverser = traverser.node
                        traverser.node = AdjNode(int(token.strip()))

    def BFS(self, s):
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
            traverser = self.adjacency_lists[u]
            while traverser.node is not None:
                v = traverser.node.vertex
                if color[v] == Color.WHITE:
                    color[v] = Color.GREY
                    distance[v] = distance[u] + 1
                    predecessor[v] = u
                    Q.append(v)
                traverser = traverser.node
            color[u] = Color.BLACK
            order.append(u)
        return order, color, predecessor, distance

    def DFS(self):
        order = list()
        color = dict()
        predecessor = dict()
        discovered = dict()
        finished = dict()
        for u in self.vertices:
            color[u] = Color.WHITE
            predecessor[u] = None
        time = 0
        for u in self.vertices:
            if color[u] == Color.WHITE:
                self.DFS_visit(u, time, order, color, predecessor, discovered, finished)
        return order, color, predecessor, discovered, finished

    def DFS_visit(self, u, time, order, color, predecessor, discovered, finished):
        color[u] = Color.GREY
        time += 1
        discovered[u] = time
        traverser = self.adjacency_lists[u]
        while traverser.node is not None:
            v = traverser.node.vertex
            if color[v] == Color.WHITE:
                predecessor[v] = u
                self.DFS_visit(v, time, order, color, predecessor, discovered, finished)
            traverser = traverser.node
        color[u] = Color.BLACK
        order.append(u)
        time += 1
        finished[u] = time
        return None


class AdjNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.node = None

    def __str__(self):
        traverser = self.node
        node_str = ""
        while traverser is not None:
            node_str += f"{traverser.vertex}, "
            traverser = traverser.node
        return node_str[:-2]

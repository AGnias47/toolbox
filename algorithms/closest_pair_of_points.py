#!/usr/bin/env python

import math


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def one_d(points):
    smallest_distance = math.inf
    sorted_points = sorted(points)
    pair = (None, None)
    for i in range(len(sorted_points) - 1):
        d = abs(sorted_points[i] - sorted_points[i + 1])
        if d < smallest_distance:
            smallest_distance = d
            pair = (sorted_points[i], sorted_points[i + 1])
    return pair, smallest_distance


def brute_force(points):
    smallest_distance = math.inf
    pair = (None, None)
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            d = distance(points[i], points[j])
            if d < smallest_distance:
                pair = (points[i], points[j])
                smallest_distance = d
    return pair, smallest_distance


if __name__ == "__main__":
    print("1D Example")
    sample = [1, 3, 7, 21, 23]
    print(one_d(sample))
    print("2D Brute Force Example")
    sample = [(1, 1), (1, 2), (3, 4), (5, 1), (2, 2)]
    print(brute_force(sample))

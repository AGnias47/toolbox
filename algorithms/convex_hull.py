#!/usr/bin/env python


def point_side(p1, p2, p3):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p1[0], p3[1] - p1[1])
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]
    if cross_product > 0:
        return 1
    elif cross_product < 0:
        return -1
    else:
        return 0


def brute_force(points):
    convex_hull = []
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                p1 = points[i]
                p2 = points[j]
                left = []
                right = []
                for k in range(len(points)):
                    side = point_side(p1, p2, points[k])
                    if side > 0:
                        right.append(points[k])
                    elif side < 0:
                        left.append(points[k])
                    if len(left) == 0 or len(right) == 0:
                        if p1 not in convex_hull:
                            convex_hull.append(p1)
                        if p2 not in convex_hull:
                            convex_hull.append(p2)
    return convex_hull


if __name__ == "__main__":
    sample = [(1, 1), (1, 2), (3, 4), (5, 1), (2, 2)]
    print(brute_force(sample))

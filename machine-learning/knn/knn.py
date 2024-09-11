from collections import Counter, namedtuple
from math import sqrt

Point = namedtuple("Point", ["x", "y", "label"])
Distance = namedtuple("Distance", ["point", "distance"])


def euclidean_distance(p1, p2):
    return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def knn(data, p, k=3):
    distances = []
    for point in data:
        p_d = euclidean_distance(point, p)
        distances.append(Distance(point, p_d))
    sorted(distances, key=lambda x: x.distance)
    labels = Counter(x.point.label for x in distances[:k])
    return labels.most_common()[0][0]


if __name__ == "__main__":
    points = [
        Point(1, 1, "x"),
        Point(1, 0, "x"),
        Point(3, 4, "o"),
        Point(4, 7, "o"),
        Point(5, 6, "o"),
        Point(6, 5, "x"),
        Point(7, 9, "o"),
        Point(3, 4, "o"),
    ]
    print(knn(points, Point(1, 0, None)))

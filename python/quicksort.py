#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]


def quicksort(A):
    if len(A) > 1:
        pivot = A[0]
        g, l, e = list(), list(), list()
        for n in A:
            if n > pivot:
                g.append(n)
            elif n < pivot:
                l.append(n)
            else:
                e.append(n)
        return quicksort(l) + e + quicksort(g)
    else:
        return A


if __name__ == "__main__":
    print(quicksort([5, 7, 2, 6, 4, 2, 5, 2, 1]))

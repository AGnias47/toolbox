#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from math import inf
from copy import deepcopy


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


def insertion_sort(A):
    for i, j in enumerate(A):
        if i == 0:
            pass
        else:
            key = j
            z = i - 1
            while z > -1 and A[z] > key:
                A[z + 1] = A[z]
                z -= 1
            A[z + 1] = key
    return A


def _merge(A, l, m, r):
    n1 = m - l + 1  # Last element for left array
    n2 = r - m  # Last element for right array
    L = [inf] * (n1)  # Initialize to length, with inf as last element
    R = [inf] * (n2)  # Initialize to length, with inf as last element
    for i in range(0, n1):  # Create left array
        L[i] = A[l + i]
    for j in range(0, n2):
        R[j] = A[m + j + 1]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1


def merge_sort(A, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(A, l, m)
        merge_sort(A, m + 1, r)
        _merge(A, l, m, r)


def counting_sort(A, a_max):
    sorted_output = [0] * len(A)
    working_storage = [0] * (a_max + 1)  # Initialize counts to 0 for all ints in range
    for element in A:
        working_storage[element] += 1  # Get counts for each int
    for i in range(1, a_max + 1):  # set working_storage to the number of elements <= i
        working_storage[i] = working_storage[i] + working_storage[i - 1]
    for i in range(len(A) - 1, -1, -1):
        # A[i] = int in A at i
        # working_storage[A[i]] = Sorted position of that int
        # sorted_output[working_storage[A[i]]] = index in the sorted array where A[i] should go
        sorted_output[working_storage[A[i]] - 1] = A[i]
        working_storage[A[i]] -= 1
    return sorted_output


if __name__ == "__main__":
    A1 = [5, 7, 2, 6, 4, 2, 5, 2, 1]
    print(quicksort(A1))
    print(insertion_sort(A1))
    print(counting_sort(A1, max(A1)))
    A_1 = deepcopy(A1)
    merge_sort(A_1, 0, len(A_1) - 1)
    print(A_1)

from random import randint

def nonrecursive_binary_search(A, b):
    left_index = 0
    right_index = len(A) - 1
    while left_index <= right_index:
        index = (left_index + right_index) // 2
        if A[index] == b:
            return index
        elif A[index] > b:
            right_index = index - 1
        else:
            left_index = index + 1
    return -1

def recursive_binary_search(A, start, end, b):
    if start != end:
        mid_index = (start + end) // 2
        if A[mid_index] == b:
            return mid_index
        elif A[mid_index] > b:
            return recursive_binary_search(A, start, mid_index, b)
        else:
            return recursive_binary_search(A, mid_index+1, end, b)
    else:
        if A[start] == b:
            return start
        else:
            return -1

for i in range(0, 1000):
    A = [1, 3, 5, 7, 9]
    b = randint(0, 10)
    result_r = recursive_binary_search(A, 0, len(A) - 1, b)
    result_nr = nonrecursive_binary_search(A, b)
    for result in {result_r, result_nr}:
        if result == -1:
            assert b not in A
        else:
            assert A[result] == b


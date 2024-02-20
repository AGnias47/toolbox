#!/usr/bin/env python


def merge_and_count(a, b):
    current = 0
    count = 0
    output = []
    while a and b:
        if a[current] <= b[current]:
            output.append(a.pop(current))
        else:
            output.append(b.pop(current))
            count += len(a)
    if a:
        output += a
    if b:
        output += b
    return output, count


def sort_and_count(lst):
    if len(lst) <= 1:
        return lst, 0
    a, a_c = sort_and_count(lst[: len(lst) // 2])
    b, b_c = sort_and_count(lst[len(lst) // 2 :])
    r, c = merge_and_count(a, b)
    return r, a_c + b_c + c


if __name__ == "__main__":
    lst = [1, 2, 4, 3, 5]
    print(sort_and_count(lst))

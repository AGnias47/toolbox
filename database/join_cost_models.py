from math import ceil, log


def block_nested_loop_cost(b_r, b_s, B):
    return ceil(b_r / B - 2) * b_s + b_r


def sort_merge_join_cost(b_r, b_s, B):
    b_r_sort_cost = b_r * (2 * ceil(log(b_r / B, B - 1)) + 1)
    b_s_sort_cost = b_s * (2 * ceil(log(b_s / B, B - 1)) + 1)
    merge_join_cost = b_r + b_s
    return b_r_sort_cost + b_s_sort_cost + merge_join_cost

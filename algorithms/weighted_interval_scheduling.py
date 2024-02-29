#!/usr/bin/env python3


def compute_opt(j, V, P, M):
    """
    From p. 256 of Algorithm Design by J. Kleinberg and E. Tardos. Computes the
    max weight for weighted interval scheduling.

    Parameters
    ----------
    j: int
        Index of interval
    V: list
        Array of weights for each interval, with index 0 being a sentinel value
    P: list
        Array pointing to the closest previous index that is disjoint with the current interval.
        If none exists, the value is 0.
    M: list
        Memoization array

    Returns
    -------
    int
    """
    if j == 0:
        return 0
    if M[j] == 0:
        M[j] = max(V[j] + compute_opt(P[j], V, P, M), compute_opt(j - 1, V, P, M))
    return M[j]


def find_solution(j, V, P, M):
    """
    From p. 258 of Algorithm Design by J. Kleinberg and E. Tardos.
    Uses the memoized values to give the schedule with max weight.

    Parameters
    ----------
    j: int
        Index of interval
    V: list
        Array of weights for each interval, with index 0 being a sentinel value
    P: list
        Array pointing to the closest previous index that is disjoint with the current interval.
        If none exists, the value is 0.
    M: list
        Memoization array

    Returns
    -------
    list
        Indices of schedule with max weight
    """
    if j == 0:
        return []
    if V[j] + M[P[j]] >= M[j - 1]:
        return [j] + find_solution(P[j], V, P, M)
    else:
        return find_solution(j - 1, V, P, M)


if __name__ == "__main__":
    V = [0, 2, 4, 4, 7, 2, 1]
    P = [0, 0, 0, 1, 0, 3, 3]
    n = len(V) - 1
    M = [0] * (n + 1)
    max_weight = compute_opt(n, V, P, M)
    schedule_indexes = find_solution(n, V, P, M)
    print(f"Schedule {schedule_indexes} has a max weight of {max_weight}")

#!/usr/bin/env python3

SENTINEL = 0

low_stress = [SENTINEL, 10, 1, 10, 10]
high_stress = [SENTINEL, 5, 50, 5, 1]
n = len(low_stress) - 1
M = [None] * (n + 1)


def plan(n, next_job_high=False):
    if n == 1:
        if next_job_high:
            return 0
        M[n] = max(low_stress[n], high_stress[n])
    elif not M[n]:
        if next_job_high:
            M[n] = 0 + plan(n - 1, False)
        elif low_stress[n] > high_stress[n]:
            M[n] = low_stress[n] + plan(n - 1, False)
        else:
            M[n] = high_stress[n] + plan(n - 1, True)
    return M[n]


if __name__ == "__main__":
    print(plan(n))
    print(M[1:])

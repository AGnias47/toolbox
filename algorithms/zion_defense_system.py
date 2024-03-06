#!/usr/bin/env python

SENTINEL = 0


def emp(j):
    return 2 ** (j - 1)


def destroy_robots(x, j):
    return min(x, emp(j))


def emp_planner(robot_arrivals):
    n = len(robot_arrivals[1:])
    if n == 1:
        return destroy_robots(robot_arrivals[1], 1)
    j = 0
    while j < n:
        if destroy_robots(robot_arrivals[j+1], j) <= robot_arrivals[j+1]:
            j += 1
    print(j)
    robots_destroyed = destroy_robots(robot_arrivals[j], j)
    if j < n:
        print(robot_arrivals[j :])
        robots_destroyed += destroy_robots([SENTINEL].extend(robot_arrivals[j :]))
    return robots_destroyed


def we_can_pseudo_work_with_this(n, robot_arrivals, M=None):
    W = len(robot_arrivals[1:])
    if not M:
        M = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n):
        for w in range(W + 1):
            destroyed = destroy_robots(robot_arrivals[i], i)
            if destroyed > emp_planner(n+1, robot_arrivals[i:], M):
                M[i][w] = destroyed
            else:
                M[i][w] = M[i - 1][w]
    return M[n][W]

def bad_emp_planner(robot_arrivals):
    n = len(robot_arrivals[1:])
    j = 1
    while j <= n:
        if emp(j) >= robot_arrivals[n]:
            robots_destroyed = destroy_robots(robot_arrivals[n], n)
            break
        j += 1
    else:
        j -= 1
        robots_destroyed = destroy_robots(robot_arrivals[n], n)
    if n - j >= 1:
        robots_destroyed += bad_emp_planner(robot_arrivals[: n - j + 1])
    return robots_destroyed


if __name__ == "__main__":
    s1 = [SENTINEL, 1, 10, 10, 1]  # 5
    s2 = [SENTINEL, 1, 1, 4, 2]  # 5
    for robot_schedule in [s1, s2]:
        #print(bad_emp_planner(robot_schedule))
        print(emp_planner(robot_schedule))

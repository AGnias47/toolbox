#!/usr/bin/env python

SENTINEL = 0


def emp(j):
    return 2 ** (j - 1)


def destroy_robots(x, j):
    return min(x, emp(j))


def emp_planner(robot_arrivals):
    for i in range(1, len(robot_arrivals)):
        print(robot_arrivals[i])


def bad_emp_planner(robot_arrivals):
    robots_destroyed = 0
    n = len(robot_arrivals[1:])
    j = 1
    while j <= n:
        if emp(j) >= robot_arrivals[n]:
            robots_destroyed += destroy_robots(robot_arrivals[n], n)
            break
        j += 1
    else:
        j -= 1
        robots_destroyed += destroy_robots(robot_arrivals[n], n)
    if n - j >= 1:
        robots_destroyed += bad_emp_planner(robot_arrivals[: n - j+1])
    return robots_destroyed


if __name__ == "__main__":
    robot_schedule = [SENTINEL, 1, 10, 10, 1]  # 5
    print(bad_emp_planner(robot_schedule))
    robot_schedule = [SENTINEL, 1, 1, 4, 2]  # 5
    print(bad_emp_planner(robot_schedule))

#!/usr/bin/env python3

from typing import List, Set


class Request:
    def __init__(self, duration: int, deadline: int):
        self.duration = duration
        self.deadline = deadline
        self.start_time = None
        self.end_time = None
        self.late = None

    def __repr__(self):
        duration = f"Duration: {self.duration}\n"
        deadline = f"Deadline: {self.deadline}\n"
        start_time = f"Start Time: {self.start_time}\n"
        end_time = f"End Time: {self.end_time}\n"
        late = f"Late by: {self.late}\n"
        return "Request:\n" + duration + deadline + start_time + end_time + late

    def __lt__(self, other):
        return self.deadline < other.deadline


def schedule(R: Set) -> List:
    s = []
    start_time = 0
    for r in sorted(list(R)):
        r.start_time = start_time
        r.end_time = start_time + r.duration
        r.late = max(r.end_time - r.deadline, 0)
        start_time += r.duration
        s.append(r)
    return s


if __name__ == "__main__":
    r1 = Request(1, 10)
    r2 = Request(3, 5)
    r3 = Request(6, 8)
    R = {r1, r2, r3}
    print("Requests")
    print(*sorted(list(R)), sep="\n")
    A = schedule(R)
    print("Scheduled Requests")
    print(*A, sep="\n")
    print(f"Total Lateness: {sum(r.late for r in A)}")

#!/usr/bin/env python

n = None  # Number of video streams
# no delays can occur between end of one and start of next
# starts at 0, ends at sum of time for all video

# r is set such that total bits sent cannot exceed rt for all t > 0
r = 5000


class Stream:
    def __init__(self, bits, seconds):
        self.bits = bits
        self.seconds = seconds


def is_valid(schedule):
    t = 0
    b = 0
    for s in schedule:
        b_s = s.bits / s.seconds
        for i in range(s.seconds):
            b += s.bits
            t += s.seconds
            if b > r * t:
                return False
    return True


s1 = Stream(2000, 1)
s2 = Stream(6000, 2)
s3 = Stream(2000, 1)

print(is_valid([s1, s2, s3]))

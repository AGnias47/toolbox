#!/usr/bin/env python

# For n video streams
# no delays can occur between end of one and start of next
# starts at 0, ends at sum of time for all video
# r is set such that total bits sent cannot exceed rt for all t > 0


class Stream:
    def __init__(self, bits, seconds):
        self.bits = bits
        self.seconds = seconds
        self.bit_rate = self.bits / self.seconds

    def __repr__(self):
        return f"Stream: {self.bits} bits over {self.seconds} seconds"

    def __lt__(self, o):
        return self.bit_rate < o.bit_rate


def schedule(streams, r=5000):
    sorted_streams = sorted(streams)
    t = 0
    b = 0
    for s in sorted_streams:
        for i in range(s.seconds):
            b += s.bit_rate
            t += 1
            if b > r * t:
                return []
    return sorted_streams


s1 = Stream(2000, 1)
s2 = Stream(6000, 2)
s3 = Stream(2000, 1)

print(schedule([s1, s2, s3]))

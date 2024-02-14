#!/usr/bin/env python


def is_subsequence(s_pr, s):
    m = len(s_pr)
    i = 0
    for c in s:
        if s_pr[i] == c:
            i += 1
            if i == m:
                return True
    return False

# True
s_pr = "abbc"
s = "abccdbc"
print(s_pr, s)
print(is_subsequence(s_pr, s))

# False
s_pr = "abbc"
s = "abccdbxx"
print(s_pr, s)
print(is_subsequence(s_pr, s))

# True (equal to each other)
s_pr = "abccdbc"
s = "abccdbc"
print(s_pr, s)
print(is_subsequence(s_pr, s))


"""
Call a function F in a loop.
F returns a string of 140 chars.
Write to the output 1 when F returns a string with the same letters
(basically a permutation) of a string previously returned.
"""

def isPermutation(s1, s2):
    if not s1 or not s2:
        return None

    tabel = {}

    for ch in s1:
        if ch in tabel:
            tabel[ch] += 1
        else:
            tabel[ch] = 1

    for ch in s2:
        if ch in tabel and tabel[ch] > 0:
            tabel[ch] -= 1
        else:
            return False
    return True

print isPermutation("sumit", "tiums")
""" Implement a function nondecreasing_subsequences() that,
given a sequence of numbers such as: [ 3,6,61,6,7,9,1,7,7,2,7,7,2,388,3,72,7 ] ...
will identify and return each contiguous sub-sequence of non-decreasing numbers.
E.g. this example input should return this array-of-arrays (e.g. or list-of-lists)
[ [3,6,61],[6,7,9],[1,7,7],[2,7,7],[2,388],[3,72],[7] ]
(Each array includes a sequence of numbers that do not get smaller. The original order is unchanged.)
For a visual example of a non-decreasing, see: http://en.wikipedia.org/wiki/File:Monotonicity_example1.png
https://www.glassdoor.com/Interview/Implement-a-function-nondecreasing-subsequences-that-given-a-sequence-of-numbers-such-as-3-6-61-6-7-9-1-7-7-2-7-7-QTN_739223.htm
"""


def nondecreasing_subsequences(arr):
    curr = arr[0]
    res = []
    iner = [curr]
    for i in range(1, len(arr)):
        if curr <= arr[i]:
            iner.append(arr[i])
        else:
            res.append(iner)
            iner = [arr[i]]
        curr = arr[i]

    if len(iner) > 0:
        res.append(iner)

    return res


arr = [3, 6, 61, 6, 7, 9, 1, 7, 7, 2, 7, 7, 2, 388, 3, 72, 7]
print nondecreasing_subsequences(arr)

# http://www.geeksforgeeks.org/print-increasing-sequences-length-k-first-n-natural-numbers/
def printSequence(k, n):
    res = [0] * n
    printSequenceUntil(k, n, 0, res)

def printSequenceUntil(k, n, l, arr):
    if l == k:
        print arr

    i = 1
    if l > 0:
        i = arr[l-1] + 1

    l += 1

    while i <= n:
        arr[l-1] = i
        printSequenceUntil(k, n, l, arr)
        i += 1

    l -= 1

#printSequence(2, 3)
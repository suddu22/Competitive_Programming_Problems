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

    res = []
    current = arr[0]
    sub = [current]
    for num in arr[1:]:
        if num >= current:
            sub.append(num)
        else:
            res.append(list(sub))
            sub = [num]
        current = num
    if sub:
        res.append(list(sub))

    return res

arr = [3, 6, 61, 6, 7, 9, 1, 7, 7, 2, 7, 7, 2, 388, 3, 72, 7]
print nondecreasing_subsequences(arr)
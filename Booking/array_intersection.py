# coding=utf-8
"""
A multiset or a bag is a collection of elements that can be repeated.
Contrast with a set, where elements cannot be repeated.
Multisets can be intersected just like sets can be intersected.

Input :

A = [0,1,1,2,2,5]
B = [0,1,2,2,2,6]

Output :
A ∩ B = C = [0,1,2,2]

Input :
A = [0,1,1]
B = [0,1,2,3,4,5,6]

Output
A ∩ B = C = [0,1]

Write a function to find the intersection of two integer arrays in that way ?
http://www.careercup.com/question?id=5158359730749440
"""

"""
Intersection of two unsorted arrays
T: O(n)
S: O(n)
"""
def intersect(a, b):

    dict = {}
    res = []
    for n in a:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    for n in b:
        if n in dict and dict[n] > 0:
            res.append(n)
            dict[n] -= 1

    return res

A = [7, 1, 5, 2, 3, 6]
B = [3, 8, 6, 20, 7]
print "=== intersect ==="
print intersect(A, B)
"""
Intersection of two sorted arrays
T: O(m+n)
S: 1
"""
def intersect2(a, b):
    res = []
    an = len(a)
    bn = len(b)

    i = 0
    j = 0

    while i < an and j < bn:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            res.append(a[i])
            i += 1
            j += 1
    return res

A = [1,1,2,2,5]
B = [0,1,2,2,2,6]

print "=== intersect2 ==="
print intersect2(A, B)

"""
When one array is much longer than the other we should try to avoid a linear iteration over the longer one.

Since arrays are sorted, we can do a linear iteration over the shorter,
and perform binary search for it on the longer array while storing all the matches.

Runtime Complexity: O(n⋅log m). Since m ≫ n and m ≫ log m, O(n⋅log m) should be asymptotically better than O(n+m).
"""
def intersect3(small, large):
    res = []
    for num in small:
        found = binarySearch(large, num)
        if found != -1:
            res.append(num)

    return res


def binarySearch(arr, num):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (left + right)/2
        if arr[mid] > num:
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            return mid - 1
    return -1

A = [0,1,2,5,6,7]
B = [1,2,3,6,7,8,9,10,11,12,13]

A = [1,1,2,2,5]
B = [0,1,2,2,2,6]
print "=== intersect3 ==="
print intersect3(A, B)

"""
Union of two sorted arrays
Time Complexity: O(m+n)
"""
def union(a, b):
    res = []
    an = len(a)
    bn = len(b)

    i = 0
    j = 0

    while i < an and j < bn:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        elif a[i] > b[j]:
            res.append(b[j])
            j += 1
        else:
            res.append(a[i])
            i += 1
            j += 1

    while i < an:
        res.append(a[i])
        i += 1

    while j < bn:
        res.append(b[j])
        j += 1

    return res

A = [1, 3, 4, 5, 7]
B = [2, 3, 5, 6]
#print union(A, B)
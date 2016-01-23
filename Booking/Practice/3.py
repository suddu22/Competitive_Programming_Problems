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

def array_intersection(a1, a2):
    if not a1 or not a2:
        return None

    table = {}
    res = []
    for num in a1:
        if num not in table:
            table[num] = 1
        else:
            table[num] += 1

    for num in a2:
        if num in table and table[num] > 0:
            res.append(num)
            table[num] -= 1

    return res

A = [0,1,1,2,2,5]
B = [0,1,2,2,2,6]
print array_intersection(A, B)


def array_intersection_sorted(a1, a2):
    if not a1 or not a2:
        return None
    res = []
    n = len(a1)
    m = len(a2)
    i = 0
    j = 0
    while i < n and j < m:
        if a1[i] == a2[j]:
            res.append(a1[i])
            i += 1
            j += 1
        elif a1[i] > a2[j]:
            j += 1
        else:
            i += 1

    return res

B = [0,1,1,2,2,5]
A = [0,1,2,2,2,6,]
print array_intersection_sorted(A, B)

def array_intersection_sorted_larger(l, s):
    if not l or not s:
        return None
    res = []
    for num in s:
        found = array_intersection_binarySearc(l, num)
        if found != -1:
            res.append(found)
    return res

def array_intersection_binarySearc(l, num):

    n = len(l)
    left = 0
    right = n-1

    while left < right:
        mid = (left + right)/2
        if l[mid] == num:
            return num
        elif l[mid] > num:
            right = mid - 1
        else:
            left = mid + 1

    return -1

A = [0,1,1,2,2,5]
B = [0,1,2,2,2,6]
print array_intersection_sorted_larger(A, B)
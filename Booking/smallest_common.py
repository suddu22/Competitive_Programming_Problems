"""
Given two lists of integers.
Find the smallest common element.
Improvised the question to find n smallest common elements in the list.
"""
import sys
import heapq

def smallestCommon(a1, a2):

    #occurance = set()
    smallest = sys.maxint

    #for n in a1:
    #    occurance.add(n)

    for n in a2:
        if n in a1:
            if smallest > n:
                smallest = n

    return smallest

def commenElements(a1, a2):

    dict = {}
    res = []

    for n in a1:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    for n in a2:
        if n in dict and dict[n] > 0:
            res.append(n)
            dict[n] -= 1

    return res


def smallestCommonNElements(a1, a2, k):
    comon = commenElements(a1, a2)
    nsmallest = []

    if len(comon) <= k:
        return comon

    for i in range(k):
        heapq.heappush(nsmallest, -comon[i])

    for i in range(k, len(comon)):
        heapq.heappush(nsmallest, -comon[i])
        heapq.heappop(nsmallest)

    while len(nsmallest) > 0:
        print -heapq.heappop(nsmallest),

a1 = [3,6,8,9,2,4]
a2 = [1,3,4,5,6,7,8,9]

print smallestCommonNElements(a1, a2, 2)
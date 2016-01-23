# coding=utf-8
"""
Given an infinite stream of integers, find the k’th largest element at any point of time.

Example:

Input:
stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
k = 3

Output: {_,   _, 10, 11, 20, 40, 50,  50, ...}
"""
import heapq
def kthLargestStream(stream, k):
    klist = [0] * k
    n = len(stream)
    for i in range(n):
        klist.pop()
        klist.append(stream[i])
        klist.sort(reverse=True)

        print '_' if klist[k-1] is 0 else klist[k-1],

def kthLargestStream2(stream, k):
    slist = []
    for i in range(k-1):
        heapq.heappush(slist, stream[i])
        print '_',

    for i in range(k-1, len(stream)):
        heapq.heappush(slist, stream[i])

        print heapq.heappop(slist),



stream = [10, 20, 11, 70, 50, 40, 100, 5]
kthLargestStream2(stream, 3)
print
stream = [10, 20, 11, 70, 50, 40, 100, 5]
kthLargestStream(stream, 3)

ss = set()
ss.add()
ss.remove("ff")
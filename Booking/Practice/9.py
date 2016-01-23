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
class kthLargest:
    def __init__(self, k):
        self.k = k
        self.num_heap = []

    def addNumber(self, num):
        if len(self.num_heap) >= self.k:
            heapq.heappush(self.num_heap, num)
            heapq.heappop(self.num_heap)
        else:
            heapq.heappush(self.num_heap, num)

    def getKth(self):
        n = len(self.num_heap)
        if n >= self.k:
            print self.num_heap[0],
        else:
            print "_",

stream = [10, 20, 11, 70, 50, 40, 100, 5]
obj = kthLargest(3)
for num in stream:
    obj.addNumber(num)
    obj.getKth()
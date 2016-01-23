"""
Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 4
Output: 10
"""

def getKthElement(arr, k):
    if not arr:
        return None

    pivot = arr[0]
    index = 0

    for i in range(len(arr)):
        if arr[i] > pivot:
            index += 1
            arr[i], arr[index] = arr[index], arr[i]

    arr[0], arr[index] = arr[index], arr[0]

    if index + 1 == k:
        return pivot
    elif k < index + 1:
        return getKthElement(arr[:index], k)
    else:
        return getKthElement(arr[index+1:], k - index - 1)

arr = [7, 10, 4, 3, 20, 15]
k = 3

print getKthElement(arr, k)

arr = [7, 10, 4, 3, 20, 15]
k = 4

print getKthElement(arr, k)
print

import heapq
"""
T: O(n)
S: O(n)
"""
def findKthLargest(nums, k):
    heap = []

    for i in nums:
        heapq.heappush(heap, i)

    for j in range(k-1):
        heapq.heappop(heap)

    return heap
# 3 4 7 10 15 20
arr = [7, 10, 4, 3, 20, 15]
k = 3

print findKthLargest(arr, k)

arr = [7, 10, 4, 3, 20, 15]
k = 4

print findKthLargest(arr, k)
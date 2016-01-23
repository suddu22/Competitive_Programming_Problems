"""
K-Messed Array Sort

Given an array arr of length n where each element is at most k places away from its sorted position,
Plan and code an efficient algorithm to sort arr.
Analyze the runtime and space complexity of your solution.

Example: n=10, k=2. The element belonging to index 6 in the sorted array, may be at indices 4, 5, 6,7 or 8 on the given array.
"""
# Ex: 2 3 1 4 7 5 6 , k = 2
# http://www.sorting-algorithms.com/

# T: O(n log k)
# S: O(k)
import heapq

def insertionSort(arr, k):
    if not arr:
        return None
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > arr[i]:
            arr[j+1] = arr[j]
            arr[j] = x
            j -= 1
    return arr

def KMessed(arr, k):
    if not arr:
        return None

    hlist = []
    for i in range(k):
        heapq.heappush(hlist, arr[i])

    for i in range(k, len(arr)):
        heapq.heappush(hlist, arr[i])
        element = heapq.heappop(hlist)
        arr[i - k] = element

    while len(hlist) > 0:
        element = heapq.heappop(hlist)
        arr[len(arr) - len(hlist)-1] = element

    return arr

arr = [2, 3, 1, 4, 7, 5, 6]
print KMessed(arr, 2)
print insertionSort(arr, 2)
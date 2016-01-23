"""
Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 4
Output: 10
"""
import heapq

"""
T: O(n)
S: O(n)
"""
def findKthLargest(nums, k):
    heap = []

    for i in nums:
        heapq.heappush(heap, i)

    for j in range(k):
        pop = heapq.heappop(heap)

    return pop

alist = [7, 10, 4, 3, 20, 15]
#print(findKthLargest(alist, 3))

"""
T: O(n)
S: O(1)
"""
def findkthLargest2(nums, k):
    pivot = nums[0]
    start = 0

    for i in range(len(nums)):
        if nums[i] > pivot:
            start += 1
            nums[i], nums[start] = nums[start], nums[i]

    nums[0], nums[start] = nums[start], nums[0]

    if start + 1 == k:
        return nums[start]
    elif start + 1 > k:
        return findkthLargest2(nums[:start], k)
    else:
        return findkthLargest2(nums[start+1:], k - start - 1)

arr = [7, 10, 4, 3, 20, 15]
k = 3

print findkthLargest2(arr, k)

arr = [7, 10, 4, 3, 20, 15]
k = 4

print findkthLargest2(arr, k)
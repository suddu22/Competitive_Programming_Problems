def largestContinuousSum(arr):
    if len(arr) == 0:
        return None

    max_sum = arr[0]
    cur_sum = arr[0]

    for num in arr[1:]:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(cur_sum, max_sum)

    return max_sum


print(largestContinuousSum([5, 7, -13, 10, 5]))

"""
There are two steps:
1. Create cumulative sum array where ith index in this array represents total sum from 1 to ith index element.
2. Iterate all elements of cumulative sum array and use hashing to find
   two elements where value at ith index == value at jth index but i != j.
3. IF element is not present in hash in fill hash table with current element.
"""
def lszero(A):
    if len(A) == 0:
        return None

    n = len(A)
    zsum = []
    res = []

    start = 0
    for num in A:
        start += num
        zsum.append(start)

    


    print(zsum)

print(lszero([1,2,-2,4,-4]))

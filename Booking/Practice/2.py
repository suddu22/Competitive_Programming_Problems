"""
How do you remove repeated values from a INT array, returning the resultant array in the same order as original ?
"""

def array_return_duplicate(nums):
    if len(nums) < 2:
        return nums
    res = []
    n = len(nums)
    for i in range(n):
        if nums[abs(nums[i])] > 0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
        else:
            if abs(nums[i]) not in res:
                res.append(abs(nums[i]))
    return res

nums = [1,5,2,6,8,9,1,1,10,3,2,4,1,3,11,3]
print array_return_duplicate(nums)

def array_remove_duplicate(nums):
    if len(nums) < 2:
        return nums
    table = {}
    res = []
    for num in nums:
        if num not in table:
            table[num] = 1
            res.append(num)

    return res

nums = [1,5,2,6,8,9,1,1,10,3,2,4,1,3,11,3]
print array_remove_duplicate(nums)
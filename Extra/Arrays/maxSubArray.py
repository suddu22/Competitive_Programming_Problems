"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return None

        n = len(A)
        max_sum = A[0]
        arr_sum = [0] * n

        arr_sum[0] = A[0]

        for i in range(1, n):
            arr_sum[i] = max(A[i], arr_sum[i - 1] + A[i])
            max_sum = max(max_sum, arr_sum[i])

        return max_sum

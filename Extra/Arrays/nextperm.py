# coding=utf-8
"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

The replacement must be in-place, do not allocate extra memory.

Examples:

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

20, 50, 113 → 20, 113, 50
"""


class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        n = len(A)
        if n <= 1:
            return A
        k = -1
        for i in range(n - 1):
            if A[i] < A[i + 1]:
                k = i
        if k == -1:
            A.reverse()
            return A

        for i in range(k + 1, n):
            if A[i] > A[k]:
                l = i
        A[l], A[k] = A[k], A[l]
        A[k + 1:n:1] = A[n - 1:k:-1]

        return A


s = Solution()
A = [769, 533]
print s.nextPermutation(A)

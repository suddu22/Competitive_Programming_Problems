class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        if not A:
            return A

        n = len(A)
        if n == 1:
            return A[0]

        low = 0
        high = n-1

        while low <= high:
            mid = (low+high)/2
            if A[mid-1] > A[mid] < A[mid+1]:
                return A[mid]
            elif A[0] < A[mid] and A[mid] > A[n-1]:
                low = mid + 1
            elif A[0] > A[mid] < A[n-1]:
                high = mid - 1

s = Solution()
A = [ 5137, 5525, 9511, 13269, 16255, 16700, 19870, 23034, 29247, 29934, 34583, 41585, 42598, 44113, 46035, 50147, 50737, 57084, 65916, 76905, 84098, 85912, 92081, 92257, 95449 ]
print s.findMin(A)
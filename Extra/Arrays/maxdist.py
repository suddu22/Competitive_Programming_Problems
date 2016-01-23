class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if not A:
            return None

        n = len(A)
        lmin = [0] * n
        lmax = [0] * n

        lmin[0] = A[0]
        for i in range(1, n):
            lmin[i] = min(A[i], lmin[i-1])

        lmax[n-1] = A[n-1]
        for i in range(n-2, -1, -1):
            lmax[i] = max(A[i], lmax[i+1])

        i = 0
        j = 0
        maxDiff = -1
        while j < n and i < n:
            if lmin[i] < lmax[j]:
                maxDiff = max(maxDiff, j-i)
                j = j + 1
            else:
                i = i+1;

        return maxDiff

s = Solution()
a = [3, 5, 4, 2]
print s.maximumGap(a)
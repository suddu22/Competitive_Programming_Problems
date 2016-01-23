class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        if not A:
            return []

        A = sorted(A)

        for i in range(0, len(A)-1, 2):
            A[i], A[i+1] = A[i+1], A[i]

        return A

s = Solution()
A = [ 5, 1, 3, 2, 4 ]
print s.wave(A)
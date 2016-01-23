class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):

        counts = [[0 for i in range(B)] for i in range(A)]

        for i in range(A):
            counts[i][0] = 1

        for i in range(B):
            counts[0][i] = 1

        for i in range(1, A):
            for j in range(1, B):
                counts[i][j] = counts[i-1][j] + counts[i][j-1]

        return counts[A-1][B-1]



s = Solution()
print s.uniquePaths(100, 1)
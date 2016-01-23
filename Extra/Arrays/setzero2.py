class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if not A:
            return []

        rows = len(A)
        cols = len(A[0])

        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 0:
                    self.mark(A, i, j)

        for i in range(rows):
            for j in range(cols):
                if A[i][j] == -1:
                    A[i][j] = 0

        return A

    def mark(self, matrix, i, j):

        rows = len(matrix)
        cols = len(matrix[0])

        for col in range(cols):
            if matrix[i][col] != 0:
                matrix[i][col] = -1

        for row in range(rows):
            if matrix[row][j] != 0:
                matrix[row][j] = -1

s = Solution()
A = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
]

print s.setZeroes(A)
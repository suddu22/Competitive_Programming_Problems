class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if not A:
            return []

        rows = len(A)
        cols = len(A[0])

        first_row = False
        first_col = False

        for i in range(rows):
            if A[i][0] == 0:
                first_col = True
                break

        for j in range(cols):
            if A[0][j] == 0:
                first_row = True
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0

        if first_row:
            for i in range(cols):
                A[0][i] = 0

        if first_col:
            for i in range(rows):
                A[i][0] = 0



        return A


s = Solution()
A = [
        [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]
]

print s.setZeroes(A)
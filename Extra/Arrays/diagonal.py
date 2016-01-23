class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        if not a:
            return None

        res = []
        pos = []
        n = len(a)

        # move left
        for i in range(n - 1):
            res.append([a[0][i]])
            pos.append([0, i])

        # move down
        for i in range(n):
            res.append([a[i][n - 1]])
            pos.append([i, n - 1])

        for i in range(len(pos)):
            p = pos[i]
            p[0] += 1
            p[1] -= 1
            self.addDiagonal(a, n, p, res, i)

        return res

    def addDiagonal(self, a, n, pos, res, index):
        if not self.isValidMove(a, n, pos[0], pos[1]):
            return

        res[index].append(a[pos[0]][pos[1]])
        pos[0] += 1
        pos[1] -= 1
        self.addDiagonal(a, n, pos, res, index)

    def isValidMove(self, a, n, r, c):
        if r >= 0 and c >= 0 and r < n and c < n:
            return True
        return False

    def diagonal2(self, A):
        p = len(A[0])
        res = [0] * (2 * p - 1)
        for i in range((2 * p) - 1):
            res[i] = []
        for i in range(p):
            for j in range(p):
                res[i + j].append(A[i][j])
        return res


s = Solution()
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print s.diagonal2(A)

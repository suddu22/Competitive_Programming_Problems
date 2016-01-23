class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        if not X and not Y:
            return 0

        n = len(X)
        m = len(Y)

        i = 1
        j = 1

        start = [X[0], Y[0]]
        steps_count = 0

        while i < n and j < m:
            current = [X[i], Y[j]]
            diff = [abs(start[0] - current[0]), abs(start[1] - current[1])]

            max_diff = max(diff[0], diff[1])

            steps_count += max_diff

            start = current
            i += 1
            j += 1

        return steps_count

s = Solution()
A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
print s.coverPoints(A, B)
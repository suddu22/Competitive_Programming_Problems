"""
Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

[1, 2, 3, 6, 9, 8, 7, 4, 5]

"""


class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        if not A:
            return None

        result = []
        rows = len(A)
        cols = len(A[0])

        table = {'r': 'd', 'd': 'l', 'l': 'u', 'u': 'r'}
        start = 'r'

        t = 0
        b = rows-1
        l = 0
        r = cols-1

        while t <= b and l <= r:
            if start == 'r':
                for i in range(l, r+1):
                    result.append(A[t][i])
                t += 1
                start = table[start]
            elif start == 'd':
                for i in range(t, b+1):
                    result.append(A[i][r])
                r -= 1
                start = table[start]
            elif start == 'l':
                for i in range(r, l-1, -1):
                    result.append(A[b][i])
                b -= 1
                start = table[start]
            elif start == 'u':
                for i in range(b, t-1, -1):
                    result.append(A[i][l])
                l += 1
                start = table[start]

        return result

    def generateMatrix(self, A):
        if not A:
            return None

        result = [[0 for i in range(A)] for j in range(A)]
        rows = A
        cols = A

        table = {'r': 'd', 'd': 'l', 'l': 'u', 'u': 'r'}
        start = 'r'

        t = 0
        b = rows-1
        l = 0
        r = cols-1
        index = 1
        while t <= b and l <= r:
            if start == 'r':
                for i in range(l, r+1):
                    result[t][i] = index
                    index += 1
                t += 1
                start = table[start]
            elif start == 'd':
                for i in range(t, b+1):
                    result[i][r] = index
                    index += 1
                r -= 1
                start = table[start]
            elif start == 'l':
                for i in range(r, l-1, -1):
                    result[b][i] = index
                    index += 1
                b -= 1
                start = table[start]
            elif start == 'u':
                for i in range(b, t-1, -1):
                    result[i][l] = index
                    index += 1
                l += 1
                start = table[start]

        return result


s = Solution()
A = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
print s.generateMatrix(3)
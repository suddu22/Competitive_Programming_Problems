
def rotate(matrix):
    n = len(matrix)

    for layer in range(n/2):

        first = layer
        last = n - 1 - layer
        for i in range(first ,last):
            offset = i - first
            # Top
            temp = matrix[first][i]
            # left
            matrix[first][i] = matrix[last-offset][first]
            # bottom
            matrix[last-offset][first] = matrix[last][last-offset]
            # right
            matrix[last][last-offset] = matrix[i][last]
            # top
            matrix[i][last] = temp
    return matrix

def rotate2(matrix):
    n = len(matrix)

    res = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            res[j][n-i-1] = matrix[i][j]
    return res

matrix = [
    [1, 2],
    [3, 4]
]
print rotate(matrix)

matrix = [
    [1, 2],
    [3, 4]
]
print rotate2(matrix)
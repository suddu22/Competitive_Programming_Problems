problemMatrix = [
    [1, 3, 5, 8],
    [4, 2, 1, 7],
    [4, 3, 2, 3]
]


def minPathSum(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    temp = [[0 for i in range(cols)] for j in range(rows)]

    temp[0][0] = matrix[0][0]
    for i in range(1, cols):
        temp[0][i] = temp[0][i-1] + matrix[0][i]

    for j in range(1, rows):
        temp[j][0] = temp[j-1][0] + matrix[j][0]

    for i in range(1, rows):
        for j in range(1, cols):
            temp[i][j] = matrix[i][j] + min(
                temp[i-1][j],
                temp[i][j-1]
            )

    return temp[rows-1][cols-1]


print minPathSum([[1,2],[1,1]])
problemMatrix = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]


def surroundedRegions(matrix):
    if not matrix:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "O":
                markRegions(matrix, rows, cols, i, j)

    return matrix


def markRegions(matrix, rows, cols, i, j):
    q = []
    q.insert(0, [i, j])

    while len(q) > 0:
        pop = q.pop()
        pi = pop[0]
        pj = pop[1]

        if matrix[pi][pj] == "O":
            if isValidMove(q, matrix, rows, cols, i + 1, j):
                if isValidMove(q, matrix, rows, cols, i - 1, j):
                    if isValidMove(q, matrix, rows, cols, i, j + 1):
                        if isValidMove(q, matrix, rows, cols, i, j - 1):
                            matrix[pi][pj] = "X"


def isValidMove(q, matrix, rows, cols, i, j):
    if i >= 0 and i < rows and j >= 0 and j < cols:
        q.insert(0, [i, j])
        return True
    return False


print surroundedRegions(problemMatrix)

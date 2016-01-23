# coding=utf-8
# BFS
problemMatrix = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1],
]

"""
Runtime Complexity: let n and m be the numbers of columns and rows in M respectively.
Each number in M visited a constant number of times
(once during the linear scan and up to 4 times during an island expansion)
with constant number of operations for each number.
Therefore, the runtime complexity is linear O(n⋅m).
"""


def islandCount(matrix):
    islands_count = 0

    if matrix == [] and len(matrix) < 0 and len(matrix[0]) < 0:
        return 0

    rows_count = len(matrix)
    column_count = len(matrix[0])

    for r in range(rows_count):
        for c in range(column_count):
            if matrix[r][c] == 1:
                markIsland(matrix, rows_count, rows_count, r, c)
                islands_count += 1

    return islands_count


def markIsland(matrix, rows_count, column_count, r, c):
    q = []
    q.insert(0, [r, c])
    while len(q) > 0:
        current = q.pop()
        rp = current[0]
        cp = current[1]

        # check if visited
        if matrix[rp][cp] == 1:
            matrix[rp][cp] = 2
            isValidMove(q, rows_count, column_count, rp - 1, cp)
            isValidMove(q, rows_count, column_count, rp, cp - 1)
            isValidMove(q, rows_count, column_count, rp + 1, cp)
            isValidMove(q, rows_count, column_count, rp, cp + 1)


def isValidMove(q, rows_count, column_count, r, c):
    if (r >= 0 and r < rows_count) and (c >= 0 and c < column_count):
        q.insert(0, [r, c])

print islandCount(problemMatrix)

"""
Recursive solution
"""
problemMatrix = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1],
]
def islandCount_rec(matrix):
    islands_count = 0

    if matrix != [] and len(matrix) < 0 and len(matrix[0]) < 0:
        return 0
    rows_count = len(matrix)
    column_count = len(matrix[0])

    for r in range(rows_count):
        for c in range(column_count):
            if matrix[r][c] == 1:
                markIsland_rec(matrix, rows_count, rows_count, r, c)
                islands_count += 1

    return islands_count


def markIsland_rec(matrix, rows_count, column_count, r, c):
    if r < 0 or r > rows_count-1 or c < 0 or c > column_count-1:
        return

    if matrix[r][c] != 1:
        return

    matrix[r][c] = 0
    markIsland_rec(matrix, rows_count, column_count, r - 1, c)
    markIsland_rec(matrix, rows_count, column_count, r, c - 1)
    markIsland_rec(matrix, rows_count, column_count, r + 1, c)
    markIsland_rec(matrix, rows_count, column_count, r, c + 1)

print islandCount_rec(problemMatrix)
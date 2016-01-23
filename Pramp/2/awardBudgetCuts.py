def findGrantsCap(g, b):
    if (g == [] or len(g) == 0):
        return 0
    n = len(g)
    partialSums = [0] * n
    tempSum = 0
    for i in range(n):
        tempSum = tempSum + g[i]
        partialSums[i] = tempSum
    if (partialSums[n - 1] <= b):
        return 0

    start = 0
    end = n - 1
    while (end > start):
        r = ((end + start) / 2)
        if (r > 0):
            if (cappedSum(r, partialSums, n) > b):
                if (cappedSum(r - 1, partialSums, n) < b):
                    break
                else:
                    end = r - 1
            else:
                start = r + 1

    c = (b - partialSums[r - 1]) / (n - r)
    return c


def cappedSum(i, partialSums, n):
    p1 = partialSums[i - 1]
    p2 = g[i]
    p3 = g[i] * (n - i)
    return partialSums[i - 1] + g[i] * (n - i)


g = [1, 2, 3, 4, 5, 6, 7]
b = 24

print findGrantsCap(g, b)

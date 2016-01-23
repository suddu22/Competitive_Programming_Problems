"""
https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
"""
def longestZigZag(arr):
    if not arr:
        return None

    best_len = 1
    n = len(arr)
    up = [1] * n
    down = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                up[i] = max(down[j] + 1, up[i])
            if arr[i] < arr[j]:
                down[i] = max(up[j] + 1, down[i])
        best_len = max(best_len, max(up[i], down[i]))

    return best_len

arr = [1, 7, 4, 9, 2, 5]
print longestZigZag(arr)

"""
How do you remove repeated values from a INT array, returning the resultant array in the same order as original ?
"""

def naiev():
    input = [4, 5, 6, 3, 3, 4, 5, 1, 2, 2, 5]

    result = []
    for x in input:
        if input.count(x) > 1 and result.count(x) == 0:
            result.append(x)
    print result


def removeDuplicateSorted(arr):

    if len(arr) < 2:
        return arr

    i = 1
    j = 0
    while i < len(arr):
        if arr[i] == arr[j]:
            i += 1
        else:
            j += 1
            arr[j] = arr[i]
            i += 1

    return arr[:j+1]

print removeDuplicateSorted([1,2,3,3,4,5,2])


def printDuplicate(arr):

    n = len(arr)
    for i in range(n):
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print abs(arr[i]),

printDuplicate([1,2,3,3,4,5,2])
"""
Shift the array to the right in a circular fashion.
      Example : 1 2 3 4 5 --> shift by 2 --> 4 5 1 2 3
"""
"""
Time Complexity: O(n^2)
"""
def arrayShift(arr, k):

    k %= len(arr)

    while k > 0:
        temp = arr.pop()
        arr.insert(0, temp)
        k -= 1

    return arr


def arrayShift2(arr, n, d):
    oldIndex = 0
    savedValue = arr[0]

    for i in range(n):
        p1 = oldIndex + n - d
        newIndex = p1 % n

        tmp = arr[newIndex]
        arr[newIndex] = savedValue
        savedValue = tmp

        oldIndex = newIndex

    return arr
"""
Time Complexity: O(n)
"""
def arrayShift3(arr, k):
    return arrayRightShift(arr, k, len(arr))

def arrayRightShift(arr, k, n):
    arrayShift3Rev(arr, 0, n)
    arrayShift3Rev(arr, 0, k)
    arrayShift3Rev(arr, k, n)

    return arr

def arrayLeftShift(arr, k, n):
    arrayShift3Rev(arr, 0, k)
    arrayShift3Rev(arr, k, n)
    arrayShift3Rev(arr, 0, n)

    return arr


def arrayShift3Rev(arr, i, end):
    j = end-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1
        i += 1

"""
Time Complexity: O(n)
"""
def rotateArray(a, b):
    ret = []
    b = b % len(a)
    for i in xrange(len(a)-b):
        ret.append(a[i + b])
    for i in range(b):
        ret.append(a[i])
    return ret

def rotateArray2(a, b):
    ret = []
    for i in xrange(len(a)):
        ret.append(a[(i + b) % len(a)])
    return ret


arr = [1, 2, 3, 4, 5, 6, 7]
r = arrayShift3(arr,3)
print(r)

arr = [1, 2, 3, 4, 5, 6, 7]
print(arrayShift(arr,3))

arr = [1, 2, 3, 4, 5, 6, 7]
print rotateArray(arr, 4)
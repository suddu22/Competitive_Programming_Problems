"""
Shift the array to the right in a circular fashion.
      Example : 1 2 3 4 5 --> shift by 2 --> 4 5 1 2 3
"""
"""
Time Complexity: O(n)
"""
def array_circular(arr, k):
    if not arr:
        return None

    n = len(arr)
    k = k % n

    array_circular_rec(arr, k, n)

    return arr

def array_circular_rec(arr, k, n):
    array_reverse(arr, 0, n)
    array_reverse(arr, 0, k)
    array_reverse(arr, k, n)

def array_reverse(arr, start, end):
    end -= 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5]
k = 2
print array_circular(arr, k)
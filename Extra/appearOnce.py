def appearOnce(arr, low, high):

    if low > high:
        return None
    if low == high:
        return arr[low]

    mid = (high-low)/2

    if mid % 2 == 0:
        if arr[mid] == arr[mid+1]:
            return appearOnce(arr, mid+2, high)
        else:
            return appearOnce(arr, low, mid)
    else:
        if arr[mid] == arr[mid-1]:
            return appearOnce(arr, mid+1, high)
        else:
            return appearOnce(arr, low, mid-1)

# Test Array
arr = [ 1, 1, 2, 4, 4, 5, 5, 6, 6 ]

# Function call
print appearOnce(arr, 0, len(arr)-1)

def binarySearch(alist, item):

    start = 0
    last = len(alist)-1
    found = False

    while start <= last and not found:
        mid = (start + last) / 2

        if alist[mid] == item:
            found = True
        elif alist[mid] > item:
            last = mid - 1
        else:
            start = mid + 1

    return found


def binarySearch_r(alist, item):

    if len(alist) == 0:
        return False

    mid = len(alist) / 2
    if alist[mid] == item:
        return True
    elif alist[mid] > item:
        return binarySearch_r(alist[:mid], item)
    else:
        return binarySearch_r(alist[mid+1:], item)

def binarySearch_r2(alist, item, start, end):

    if start > end:
        return False

    mid = (start + end) / 2
    if alist[mid] == item:
        return True
    elif alist[mid] > item:
        return binarySearch_r2(alist, item, start, mid-1)
    else:
        return binarySearch_r2(alist, item, mid+1, end)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch_r2(testlist, 3, 0, len(testlist)))
print(binarySearch_r2(testlist, 13, 0, len(testlist)))

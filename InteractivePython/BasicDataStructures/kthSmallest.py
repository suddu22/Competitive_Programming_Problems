# Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
def find_kth_smallest(k):
    lst = [4, 5, 6, 7, 8, 32, 1, 2, 3]
    # 1, 2, 3, 4, 5, 6, 7, 8, 32

    lst.sort()

    return lst[k - 1]


# print find_kth_smallest(2)

# Using an implementation of QuickSort

def findkth(alist, k):
    return quickSortHelper(alist, 0, len(alist) - 1, k)


def quickSortHelper(alist, first, last, k):
    splitpoint = partition(alist, first, last)

    if splitpoint + 1 == k:
        return alist[splitpoint]
    if splitpoint + 1 < k:
        return quickSortHelper(alist, splitpoint + 1, last, k)
    else:
        return quickSortHelper(alist, first, splitpoint - 1, k)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:  # leftmark <= rightmark

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [4, 5, 6, 7, 8, 32, 1, 2, 3]
print findkth(alist, 7)
print find_kth_smallest(7)

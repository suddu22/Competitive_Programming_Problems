def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, left, right):
    if left < right:
        ppoint = partition(alist, left, right)

        quick_sort_helper(alist, left, ppoint - 1)
        quick_sort_helper(alist, ppoint + 1, right)


def partition(alist, left, right):
    pivot_value = alist[0]
    left_mark = left + 1
    right_mark = right

    done = False

    while not done:

        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark += 1
        while left_mark <= right_mark and alist[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            swap(alist, right_mark, left_mark)

    swap(alist, left, right_mark)

    return right_mark


def swap(alist, f, t):
    temp = alist[f]
    alist[f] = alist[t]
    alist[t] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist)


# print(alist)

def kth_smalest(alist, k):
    return kth_smalest_helper(alist, 0, len(alist) - 1, k)


def kth_smalest_helper(alist, left, right, k):
    if left < right:
        ppoint = partition(alist, left, right)
        rank = ppoint - left + 1
        if rank == k:
            return alist[ppoint]
        elif ppoint + 1 < k:
            return kth_smalest_helper(alist, ppoint + 1, right, k - rank)
        else:
            return kth_smalest_helper(alist, left, ppoint - 1, k)


#######
import random


def partition1(arr, left, right, pivotIndex):
    arr[right], arr[pivotIndex] = arr[pivotIndex], arr[right]
    pivot = arr[right]
    swapIndex = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
            swapIndex += 1
    arr[right], arr[swapIndex] = arr[swapIndex], arr[right]
    return swapIndex


def kth_largest(alist, left, right, k):
    if not 1 <= k <= len(alist):
        return
    if left == right:
        return alist[left]

    while True:
        ran = random.randint(left, right)
        pivotIndex = partition1(alist, left, right, ran)
        rank = pivotIndex - left + 1
        if rank == k:
            return alist[pivotIndex]
        elif k < rank:
            return kth_largest(alist, left, pivotIndex - 1, k)
        else:
            return kth_largest(alist, pivotIndex + 1, right, k - rank)


alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 546, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 68, 69, 70, 72, 73, 75, 76, 77, 79, 80, 514, 85, 86, 87, 90, 91, 95, 96, 99, 104, 105, 106, 107, 109, 114, 116, 118, 1143, 120, 122, 131, 137, 143, 152, 669, 158, 160, 169, 180, 182, 197, 202, 119, 34, 218, 227, 228, 231, 235, 236, 242, 762, 252, 554, 268, 271, 631, 296, 297, 311, 315, 358, 407, 419, 451, 966, 471, 82]

print kth_largest(alist, 0, len(alist) - 1, len(alist) - 15)

#alist = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]
#print kth_smalest(alist, 10)
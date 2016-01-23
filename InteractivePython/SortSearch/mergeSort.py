def merge_sort(alist):
    n = len(alist)
    if n == 1:
        return alist

    mid = n / 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    return merge(left, right)


def merge(left, right):

    i = 0
    j = 0
    ans = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            ans.append(right[j])
            j += 1
        elif right[j] > left[i]:
            ans.append(left[i])
            i += 1
    if i < len(left):
        ans.extend(left[i:])
    if j < len(right):
        ans.extend(right[j:])

    return ans

alist = [54,26,93,17,77,31,44,55,20]
print(merge_sort(alist))
print(alist)
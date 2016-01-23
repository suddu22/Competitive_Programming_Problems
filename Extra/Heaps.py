import heapq


def dNumsx(nums, k):

    if k == 0 or not nums:
        return []

    distinct = {}
    hlist = []
    count = k
    res = []
    for i in range(len(nums)):
        num = nums[i]

        if num in distinct:
            distinct[num] += 1
        else:
            distinct[num] = 0

        count -= distinct[num]
        heapq.heappush(hlist, num)

        if len(hlist) == k:
            res.append(count)
            heapq.heappop(hlist)
            count = k

    return res


def dNums(nums, k):

    if k == 0 or not nums:
        return []

    res = []
    table = {}
    dist = 0
    n = len(nums)
    for i in range(n):
        num = nums[i]
        if num in table:
            table[num] += 1
        else:
            table[num] = 1

        if i >= k-1:
            res.append(len(table))
            index = i - (k-1)
            table[nums[index]] -= 1
            if table[nums[index]] == 0:
                del table[nums[index]]
                dist -= 1

    return res


print dNums([80, 18, 80, 80, 80, 80, 80, 80, 94, 18], 8)
# 80, 18, 80, 80, 80, 80, 80, 80
# 80 => 7
# 18 => 1

# 18, 80, 80, 80, 80, 80, 80, 94
# 80 => 6
# 18 => 1
# 94 => 1
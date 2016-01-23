"""
Given a list of alphabets and a number K.
Print all ordered permutations of length K.
"""


# O(k*n^k)
def permutations(alpha, k):
    permutations_rec(alpha, k)


def perm(alist, k, res=[]):
    if k == 0:
        print "".join(res)
        return

    for i in alist:
        nres = res + [i]
        perm(alist, k - 1, nres)
        #res.pop()


def permutations_rec(alist, k, res=[]):

    if k == 0:
        print "".join(res)
        return

    for i in alist:
        nres = res + [i]
        permutations_rec(alist, k-1, nres)

permutations(['a', 'b', 'c'], 3)


"""
Given a collection of numbers, return all possible permutations.

[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

O(n!)
"""


def permute(nums):
    if nums is [] or len(nums) == 0:
        return []
    ans = []
    sub = []
    helper(nums, ans, sub)
    return ans


def helper(nums, ans, sub):

    if len(sub) == len(nums):
        ans.append(list(sub))

    for i in range(len(nums)):
        if nums[i] not in sub:
            sub.append(nums[i])
            helper(nums, ans, sub)
            sub.pop()

print permute([1,2,3])

def permuteUnique(nums):
    if nums is None or len(nums) == 0:
        return []

    ans = []
    sub = []
    visited = [0] * len(nums)
    helperUnique(ans, sub, nums, visited, 0)
    return ans

def helperUnique(ans, sub, nums, visited, k):
    if len(sub) == len(nums):
        ans.append(list(sub))

    for i in range(len(nums)):
        if visited[i] == 1 or (i != 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0):
            continue
        visited[i] = 1
        sub.append(nums[i])
        helperUnique(ans, sub, nums, visited, i + 1)
        sub.pop()
        visited[i] = 0

print permuteUnique([1, 1, 2])
"""
Given a list of alphabets and a number K.
Print all ordered permutations of length K.
"""


def permutations(alphabets, k):
    if not alphabets or k <= 0:
        return None

    res = []
    sub = []
    permutations_rec(alphabets, k, res, sub)
    return res


def permutations_rec(alphabets, k, res, sub=[]):
    if len(sub) == k:
        res.append(list(sub))
        return

    for i in range(len(alphabets)):
        ch = alphabets[i]
        sub.append(ch)
        permutations_rec(alphabets, k, res, sub)
        sub.pop()


print permutations(['a', 'b', 'c'], 2)

"""
Given a collection of numbers, return all possible permutations.

[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

O(n!)
"""


def all_possible_permutations(nums):
    if not nums:
        return None

    res = []
    sub = []
    all_possible_permutations_rec(nums, res, sub)
    return res


def all_possible_permutations_rec(nums, res, sub):
    if len(nums) == len(sub):
        res.append(list(sub))
        return

    for i in range(len(nums)):
        num = nums[i]
        if num not in sub:
            sub.append(num)
            all_possible_permutations_rec(nums, res, sub)
            sub.pop()


print all_possible_permutations([1, 2, 3])

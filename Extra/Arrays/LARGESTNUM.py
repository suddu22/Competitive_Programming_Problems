class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        def myCompare(n1, n2):
            s1 = str(n1) + str(n2)
            s2 = str(n2) + str(n1)

            if s1 > s2:
                return -1
            elif s1 < s2:
                return 1
            else:
                return 0

        if not A:
            return None

        nums = sorted(A, cmp=myCompare)
        if nums[0] == 0:
            return 0

        return "".join([str(n) for n in nums])


s = Solution()
a = [8, 89]
print s.largestNumber(a)
a = [3, 30, 34, 5, 9]
print s.largestNumber(a)

# print sorted([3, 30, 34, 5, 9])
# print sorted(["3", "30", "34", "5", "9"], reverse=True)
print 9534330

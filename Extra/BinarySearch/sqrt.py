class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if not A:
            return A

        if A < 4:
            return 1
        low = 1
        high = A
        while low <= high:
            mid = (low+high)/2
            if (mid * mid) == A:
                return mid
            elif (mid * mid) > A:
                high -= 1
            else:
                return mid

s = Solution()
print s.sqrt(11)
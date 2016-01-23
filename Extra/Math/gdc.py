class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B == 0:
            return A
        else:
            return self.gcd(B, A%B)

        """
        while A:
            A, B = B % A, A

        return B
        """


s = Solution()
print s.gcd(54, 24)
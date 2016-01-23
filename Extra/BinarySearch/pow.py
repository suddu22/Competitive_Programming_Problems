class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 0
        elif n == 0:
            return 1
        elif n < 0:
            return 1 / self.pow(x, -n, d)

        temp = self.pow(x, n/2, d)
        if n % 2 == 1:
            return (temp * temp * x) % d
        else:
            return (temp * temp) % d

s = Solution()
print s.pow(2, 3, 3)
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes2(self, A):
        zero_count = 0

        while A != 0:
            zero_count += A / 5
            A /= 5

        return zero_count

    def trailingZeroes(self, A):

        zero_count = 0
        k = 1
        while (5**k) <= A:
            zero_count += A / (5**k)
            k += 1

        return zero_count

    def factorial(self, num):
        fact = 1
        for i in range(1, num+1):
            fact *= i
        return fact

    def factorial2(self, num):
        if num == 0:
            return 1
        return num * self.factorial(num-1)

s = Solution()
print s.trailingZeroes(3125)
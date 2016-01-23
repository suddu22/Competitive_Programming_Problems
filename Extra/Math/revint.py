"""
Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""
import sys
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if not A:
            return None
        num = A
        rev = 0
        max_int = sys.maxint
        isNegative = False

        if num < 0:
            isNegative = True
            num *= -1

        while num > 0:
            rev *= 10
            if (num % 10) + rev >= max_int:
                return 0

            rev += num % 10
            num /= 10

        if isNegative:
            rev *= -1

        return rev

s = Solution()
print s.reverse(-1146467285)
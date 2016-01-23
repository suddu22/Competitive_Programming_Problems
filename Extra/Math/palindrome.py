class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):

        return A == self.reverse_int(A)

    def reverse_int(self, num):
        rev = 0
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num /= 10

        return rev

    def isPalindrome2(self, A):
        num = str(A)
        n = len(num)
        for i in range(n/2):
            if num[i] != num[n-i-1]:
                return False
        return True

s = Solution()
print s.reverse_int(-123)
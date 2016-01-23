import re
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):

        pal = "".join(re.split('\W+', A)).lower()

        n = len(pal)
        for i in range(n/2):
            if pal[i] != pal[n-i-1]:
                return False
        return True

    def lengthOfLastWord(self, A):
        if not A:
            return 0
        length = 0
        for i in A.strip():
            if i == ' ':
                length = 0
            else:
                length += 1
        return length

s = Solution()
A = "World  "
print s.lengthOfLastWord(A)
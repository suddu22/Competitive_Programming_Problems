class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if not A:
            return None

        n = len(A)
        rem = 0
        A[-1] += 1
        for i in range(n-1, -1, -1):
            temp = A[i] + rem
            if temp > 9:
                num = temp % 10
                rem = temp - 9
            else:
                rem = 0
                num = temp
            A[i] = num
            if rem == 0:
                break
        if rem != 0:
            A.insert(0, rem)
        while A[0] == 0:
            A.pop(0)

        return A
s = Solution()
A = [0, 0, 4, 4, 6, 0, 9, 6, 5, 1]
print s.plusOne(A)
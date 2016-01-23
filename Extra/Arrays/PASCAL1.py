class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):

        res = []
        sub = []
        if A == 0:
            return []
        elif A == 1:
            return [[1]]

        for i in range(A):
            sub.append(1)
            for j in range(i-1):
                sub.append(res[i-1][j] + res[i-1][j+1])

            if i > 0:
                sub.append(1)

            res.append(list(sub))
            sub = []

        return res

s= Solution()
print s.generate(0)
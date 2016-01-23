

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        if not A:
            return None

        n = len(A)
        alpha = sorted(A)
        done_word = None
        fact = []
        for i in range(n):
            done_word = alpha[i:i+1]
            if done_word == A[i:i+1]:
                done_word = 0
            else:
                fact.append(n - len(done_word))



    def rankperm(self, perm):
        rank = 1
        suffixperms = 1
        ctr = {}
        for i in range(len(perm)):
            x = perm[((len(perm) - 1) - i)]
            if x not in ctr:
                ctr[x] = 1
            else:
                ctr[x] += 1
            for y in ctr:
                if y < x:
                    rank += ((suffixperms * ctr[y]) // ctr[x])
            suffixperms = ((suffixperms * (i + 1)) // ctr[x])
        return rank

s = Solution()
print s.rankperm("acb")


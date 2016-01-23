class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, txt, pat):
        if not txt or not pat:
            return -1

        m = len(pat)
        n = len(txt)

        for i in range(n-m+1):
            match = True
            for j in range(m):
                if txt[i+j] != pat[j]:
                    match = False
                    break
            if j == m-1 and match:
                return i

        return -1

    def rabinKarp(self, txt, pat):
        if not txt or not pat:
            return -1

        m = len(pat)
        n = len(txt)
        pat_hash = self.creatHash(pat, m - 1)
        txt_hash = self.creatHash(txt, m - 1)
        for i in range(n-m+2):
            j = i-1
            if pat_hash == txt_hash and pat == txt[j:j+m]:
                return j
            if i < n - m + 1:
                txt_hash = self.recalculateHash(txt, txt_hash, i-1, i+m-1, m)

        return -1

    def creatHash(self, txt, end):
        result_hash = 0
        prime = 101
        for i in range(end+1):
            result_hash += ord(txt[i]) * pow(prime, i)
        return result_hash

    def recalculateHash(self, txt, old_hash, old_index, new_index, path_len):
        prime = 101
        result_hash = old_hash - ord(txt[old_index])
        result_hash /= prime
        result_hash += ord(txt[new_index]) * pow(prime, path_len-1)

        return result_hash


s = Solution()
txt = "bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba"
pat = "babaaa"
print s.rabinKarp(txt, pat)
print s.strStr(txt, pat)
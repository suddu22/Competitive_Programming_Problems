class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        if not A:
            return None

        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        st = []
        for i in range(len(A)):
            ch = A[i]
            if i == len(A)-1:
                st.append(table[ch])
            else:
                new_val = table[ch]
                next_val = table[A[i+1]]
                if next_val > new_val:
                    st.append(-table[ch])
                else:
                    st.append(table[ch])
        result = 0
        while len(st) > 0:
            result += st.pop()

        return result

s = Solution()
A = "CMVI" # 906 x:1106

print s.romanToInt(A)
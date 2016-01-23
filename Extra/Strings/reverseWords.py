class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        if not A:
            return None

        n = len(A)
        self.rev(A, 0, n-1)
        start_index = 0

        for i in range(n):
            ch = A[i]
            if not str(ch).strip():
                self.rev(A, start_index, i-1)
                start_index = i+1
        self.rev(A, start_index, n-1)

        return A

    def rev(self, A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
s = Solution()
A = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', ' ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
print s.reverseWords(A)
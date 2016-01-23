class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        if not A:
            return A

        n = len(A)
        for i in range(n):
            A[i] = A[i] + (A[A[i]] % n) * n

        for i in range(n):
            A[i] = A[i] / n


        return A

s = Solution()
A = [4, 0, 2, 1, 3]
print s.arrange(A)
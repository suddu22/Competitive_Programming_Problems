class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        if not A:
            return 0

        start_index = self.binarySerach(A, B, True)
        if start_index == -1:
            return 0
        end_index = self.binarySerach(A, B, False)

        return (end_index - start_index) + 1

    def binarySerach(self, A, B, start):
        n = len(A)
        i = 0
        j = n - 1
        result = -1
        while i <= j:
            mid = (i + j) / 2
            if A[mid] == B:
                result = mid
                if start:
                    j = mid - 1
                else:
                    i = mid + 1
            elif A[mid] > B:
                j = mid - 1
            else:
                i = mid + 1
        return result

s = Solution()
A = [1,1,3,3,3,5,5,5,5,5]
print s.findCount(A, 5)
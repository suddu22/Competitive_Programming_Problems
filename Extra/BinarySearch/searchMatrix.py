class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if not A:
            return A
        rows = len(A)
        cols = len(A[0])

        for i in range(rows):
            if A[i][cols-1] >= B:
                if self.binarySearch(A[i], B) == 1:
                    return 1

        return 0

    def binarySearch(self, row, B):
        n = len(row)
        if n == 1:
            if row[0] == B:
                return 1
            else:
                return 0

        low = 0
        high = n-1

        while low <= high:
            mid = (low+high)/2
            if row[mid] == B:
                return 1
            elif row[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        return 0

    def searchMatrix2(self, A, B):
        rows = len(A)
        if rows == 0:
            return 0
        cols = len(A[0])

        low = 0
        high = (rows * cols) - 1

        while low <= high:
            mid = (low+high)/2

            i = mid/cols
            j = (mid-i*cols)

            if A[i][j] == B:
                return 1
            elif A[i][j] < B:
                low = mid + 1
            else:
                high = mid - 1
        return 0

s = Solution()
A = [
  [2, 9, 12, 13, 16, 18, 18, 19, 20, 22],
  [29, 59, 62, 66, 71, 75, 77, 79, 97, 99]
]
B = 45
print s.searchMatrix2(A, B)
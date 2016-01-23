class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if not A:
            return -1
        n = len(A)
        if n == 1:
            if A[0] == B:
                return 0
            else:
                return -1
        result = -1
        index, pivot = self.find_pivot(A)
        if pivot == B:
            return index
        else:
            result = self.binary_search(A[:index-1], B)
            if result == -1:
                result = self.binary_search(A[index:], B)
                if result != -1:
                    result += index

        return result

    def binary_search(self, arr, t):
        n = len(arr)
        low = 0
        high = n-1

        while low <= high:
            mid = (low+high)/2
            if arr[mid] == t:
                return mid
            elif arr[mid] > t:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def find_pivot(self, arr):
        n = len(arr)
        low = 0
        high = n-1

        if arr[low] <= arr[high]:
            return 0, arr[low]

        while low <= high:
            mid = (low+high)/2
            if arr[mid-1] > arr[mid] < arr[mid+1]:
                return mid, arr[mid]
            elif arr[0] < arr[mid] > arr[n-1]:
                low = mid + 1
            elif arr[0] > arr[mid] < arr[n-1]:
                high = mid - 1

        return -1,-1

s = Solution()
A = [ 19, 20, 21, 22, 28, 29, 32, 36, 39, 40, 41, 42, 43, 45, 48, 49, 51, 54, 55, 56, 58, 60, 61, 62, 65, 67, 69, 71, 72, 74, 75, 78, 81, 84, 85, 87, 89, 92, 94, 95, 96, 97, 98, 99, 100, 105, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 130, 131, 133, 134, 135, 136, 137, 138, 139, 141, 142, 144, 146, 147, 148, 149, 150, 153, 155, 157, 159, 161, 163, 164, 169, 170, 175, 176, 179, 180, 185, 187, 188, 189, 192, 196, 199, 201, 203, 205, 3, 7, 9, 10, 12, 13, 17 ]
B = 6
print s.search(A, B)
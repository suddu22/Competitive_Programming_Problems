import heapq


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m = len(A) + len(B)
        if m % 2 == 0:
            return (self.kth(A, B, m / 2) + self.kth(A, B, (m / 2) - 1)) / 2
        else:
            return self.kth(A, B, m / 2)

    def kth(self, A, B, k):
        if not A:
            return B[k]
        if not B:
            return A[k]

        midA = len(A)/2
        midB = len(B)/2

        if midA + midB < k:
            if A[midA] > B[midB]:
                return self.kth(A, B[midB+1:], k - midB -1)
            else:
                return self.kth(A[midA + 1:], B, k - midA - 1)
        else:
            if A[midA] > B[midB]:
                return self.kth(A[:midA], B, k)
            else:
                return self.kth(A, B[:midB], k)

    def findMedianSortedArrays_onlyifequal(self, A, B):
        if not A and not B:
            return None

        if len(A) == 2 and len(B) == 2:
            return (max(A[0], B[0]) + min(A[1], B[1])) / 2.0

        i1 = len(A) / 2
        i2 = len(B) / 2
        m1 = A[i1]
        m2 = B[i2]
        if m1 == m2:
            return m1
        if m1 < m2:
            return self.findMedianSortedArrays(A[i1:], B[:i2+1])
        else:
            return self.findMedianSortedArrays(A[:i1+1], B[i2:])

    def findMedianSortedArrays_slow2(self, A, B):
        if not A and not B:
            return None
        elif not A and B:
            return self.median(B)
        elif A and not B:
            return self.median(A)

        a = len(A)
        b = len(B)
        i = 0
        j = 0

        max_heap = []
        min_heap = []

        if A[i] < B[j]:
            heapq.heappush(max_heap, -A[i])
            heapq.heappush(min_heap, B[j])
        elif A[i] < B[j]:
            heapq.heappush(max_heap, -B[j])
            heapq.heappush(min_heap, A[i])
        else:
            heapq.heappush(max_heap, -B[j])
            heapq.heappush(max_heap, -A[i])
        i += 1
        j += 1

        while i < a and j < b:
            if A[i] < B[j]:
                if A[i] < -max_heap[0]:
                    heapq.heappush(max_heap, -A[i])
                    i += 1
                else:
                    heapq.heappush(min_heap, B[j])
                    j += 1
            else:
                if B[j] < -max_heap[0]:
                    heapq.heappush(max_heap, -B[j])
                    j += 1
                else:
                    heapq.heappush(min_heap, A[i])
                    i += 1

        while i < a:
            if A[i] < -max_heap[0]:
                heapq.heappush(max_heap, -A[i])
            else:
                heapq.heappush(min_heap, A[i])
            i += 1
        while j < b:
            if B[j] < -max_heap[0]:
                heapq.heappush(max_heap, -B[j])
            else:
                heapq.heappush(min_heap, B[j])
            j += 1

        while abs(len(max_heap) - len(min_heap)) > 1:
            if len(max_heap) > len(min_heap):
                pop = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, pop)
            else:
                pop = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -pop)

        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2.0
        else:
            if len(max_heap) > len(min_heap):
                return -max_heap[0]
            else:
                return min_heap[0]

    def findMedianSortedArrays_slow(self, A, B):
        if not A and not B:
            return None
        elif not A and B:
            return self.median(B)
        elif A and not B:
            return self.median(A)

        merged = self.merge(A, B)

        return self.median(merged)

    def merge(self, A, B):
        a = len(A)
        b = len(B)
        i = 0
        j = 0
        res = []
        while i < a and j < b:
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            elif A[i] > B[j]:
                res.append(B[j])
                j += 1
            else:
                res.append(A[i])
                res.append(B[j])
                i += 1
                j += 1

        while i < a:
            res.append(A[i])
            i += 1
        while j < b:
            res.append(B[j])
            j += 1

        return res

    def median(self, arr):
        n = len(arr)
        p = n / 2
        if n % 2 == 0:
            return (arr[p - 1] + arr[p]) / 2.0
        else:
            return arr[p]


s = Solution()
A = [-48, -43, 46]
B = [18, 22, 50]
print s.findMedianSortedArrays(A, B)


import heapq

"""
For the first two elements add smaller one to the maxHeap, and bigger one to the minHeap.
Then process stream data one by one:

Step 1: Add next item to one of the heaps
   If next item is smaller than maxHeap root add it to maxHeap,
   else add it to minHeap

Step 2: Balance the heaps (after this step heaps will be either balanced or
   one of them will contain 1 more item)

   if number of elements in one of the heaps is greater than the other by
   more than 1, remove the root element from the one containing more elements and
   add to the other one

To return the median:
   If the heaps contain equal elements;
     median = (root of maxHeap + root of minHeap)/2
   Else
     median = root of the heap with more elements
http://www.ardendertat.com/2011/11/03/programming-interview-questions-13-median-of-integer-stream/
"""


class RunningMedian:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.currentInput = []

    def addIntegerFromStream(self, num):

        if len(self.currentInput) == 0:
            self.currentInput.append(num)

        elif len(self.currentInput) == 1:
            prev = self.currentInput[0]
            if prev > num:
                heapq.heappush(self.maxHeap, -num)
                heapq.heappush(self.minHeap, prev)
            else:
                heapq.heappush(self.maxHeap, -prev)
                heapq.heappush(self.minHeap, num)
            self.currentInput.append(num)

        elif len(self.currentInput) >= 2:
            maxRoot = -self.maxHeap[0]

            if num < maxRoot:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)

            self.currentInput.append(num)

        while abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findCurrentMedian(self):
        minlen = len(self.minHeap)
        maxlen = len(self.maxHeap)

        if minlen == 0 and maxlen == 0 and len(self.currentInput) == 1:
            return self.currentInput[0]
        elif minlen > 0 and maxlen == 0:
            return self.minHeap[0]
        elif minlen == 0 and maxlen > 0:
            return -self.maxHeap[0]

        if minlen == maxlen:
            median = (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        elif minlen > maxlen:
            median = self.minHeap[0]
        else:
            median = -self.maxHeap[0]

        return median

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


rm = RunningMedian()

A = [-50, -41, -40, -19, 5, 21, 28]
B = [-50, -21, -10]
m = [-48, -43, 18, 29, 46]
for num in m:
    rm.addIntegerFromStream(num)
print rm.findCurrentMedian()

"""
rm.addIntegerFromStream(2)
print rm.findCurrentMedian() # 2
rm.addIntegerFromStream(3)
print rm.findCurrentMedian() # 2.5
rm.addIntegerFromStream(6)
print rm.findCurrentMedian() # 3
rm.addIntegerFromStream(1)
print rm.findCurrentMedian() # 2.5
rm.addIntegerFromStream(5)
print rm.findCurrentMedian() # 3
"""

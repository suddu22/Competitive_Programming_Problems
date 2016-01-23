class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):

        n = len(arrive)
        arrive = sorted(arrive)
        depart = sorted(depart)

        a = 0
        d = 0
        rooms = K
        while a < n and d < n:
            if arrive[a] < depart[d]:
                rooms -= 1
                a += 1
            elif arrive[a] > depart[d]:
                rooms += 1
                d += 1
            else:
                a += 1
                d += 1

            if rooms < 0:
                return False

        return True

    def hotel2(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)

        guests = 0

        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1

            if guests > K:
                return 0

        return 1


s = Solution()
A = [ 11, 24, 36, 15, 16, 23, 20, 19 ]
B = [ 14, 32, 67, 25, 21, 54, 61, 34 ]
C = 4
#print s.hotel2(A,B,C)

import math
print math.ceil(4.5)

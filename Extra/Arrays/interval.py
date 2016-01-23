"""
Lets see how we check if interval 1 (a,b) intersects with interval 2 (c,d):

Note that if max(a,c) > min(b,d), then the intervals do not overlap. Otherwise, they overlap.

Once we figure out the intervals ( interval[i] to interval[j] ) which overlap with newInterval,
note that we can replace all the overlapping intervals with one interval which would be

(min(interval[i].start, newInterval.start), max(interval[j].end, newInterval.end)).

Do make sure you cover the other corner cases.
"""

# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if not new_interval:
            return intervals
        res = []

        for curr in intervals:
            if curr.end < new_interval.start:
                res.append(curr)
            elif curr.start > new_interval.end:
                res.append(new_interval)
                new_interval = curr
            elif curr.end >= new_interval.start or curr.start <= new_interval.end:
                new_interval = Interval(min(curr.start, new_interval.start), max(curr.end, new_interval.end))

        res.append(new_interval)

        return res

    def merge(self, intervals):
        if not intervals:
            return None
        n = len(intervals)
        res = []
        intervals = sorted(intervals, key=lambda x:x.start)
        res.append(intervals[0])
        for i in range(n):
            curr = intervals[i]
            prev = res[-1]
            if curr.start <= prev.end:
                res[-1].end = max(prev.end, curr.end)
            else:
                res.append(curr)

        return res



s = Solution()
A = [ Interval(6037774, 6198243),
      Interval(6726550, 7004541),
      Interval(8842554, 10866536),
      Interval(11027721, 11341296),
      Interval(11972532, 14746848),
      Interval(16374805, 16706396),
      Interval(17557262, 20518214),
      Interval(22139780, 22379559),
      Interval(27212352, 28404611),
      Interval(28921768, 29621583),
      Interval(29823256, 32060921),
      Interval(33950165, 36418956),
      Interval(37225039, 37785557),
      Interval(40087908, 41184444),
      Interval(41922814, 45297414),
      Interval(48142402, 48244133),
      Interval(48622983, 50443163),
      Interval(50898369, 55612831),
      Interval(57030757, 58120901),
      Interval(59772759, 59943999),
      Interval(61141939, 64859907),
      Interval(65277782, 65296274),
      Interval(67497842, 68386607),
      Interval(70414085, 73339545),
      Interval(73896106, 75605861),
      Interval(79672668, 84539434),
      Interval(84821550, 86558001),
      Interval(91116470, 92198054),
      Interval(96147808, 98979097) ]
B = Interval(36210193, 61984219)


B = [Interval(4,100),Interval(6,90),Interval(30,80),Interval(1,14)]

print s.merge(B)
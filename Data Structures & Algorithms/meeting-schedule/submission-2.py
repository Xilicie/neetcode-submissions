"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        # the objective -> True if there are no overlapping intervals, else False
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        intrv = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            if intrv.end <= sorted_intervals[i].start:
                intrv = sorted_intervals[i]
            else:
                return False
        return True
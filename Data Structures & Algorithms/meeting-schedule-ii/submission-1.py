"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        min_heap = []   # stores end times

        res = 0
        n = len(intervals)

        for interval in sorted_intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)


            

        
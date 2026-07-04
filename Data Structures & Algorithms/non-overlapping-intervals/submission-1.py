class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        sorted_intervals = sorted(intervals, key=lambda x : x[1])
        # greedy approach:
        # always choose intervals with earliest finish time -> 
        
        intrv = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            if intrv[1] <= sorted_intervals[i][0]:
                intrv = sorted_intervals[i]
            else:
                res += 1
        return res

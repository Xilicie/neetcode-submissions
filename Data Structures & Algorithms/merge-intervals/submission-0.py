class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals based on start_i
        intervals = sorted(intervals)

        res = []

        i = 1
        while i < len(intervals):

            if intervals[i - 1][1] >= intervals[i][0]:
                intervals[i] = [intervals[i - 1][0], max(intervals[i - 1][1], intervals[i][1])]

            else:
                res.append(intervals[i - 1])

            i += 1

        res.append(intervals[i - 1])

        return res


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(intervals), len(queries)
        intervals.sort()

        # indices of sorted queries
        sorted_queries = [x[0] for x in sorted(enumerate(queries), key=lambda y: y[1])]

        min_heap = []
        output = [0] * m
        j = 0
        for i in sorted_queries:
            # append intervals to min_heap while intervals[j][0] <= queries[i]
            while j < n and intervals[j][0] <= queries[i]:
                size = intervals[j][1] - intervals[j][0] + 1

                heapq.heappush(min_heap, (size, intervals[j][1]))
                j += 1

            # pop intervals from min_heap while end times are less than queries[i]
            while min_heap and min_heap[0][1] < queries[i]:
                heapq.heappop(min_heap)
            
            min_size = min_heap[0][0] if min_heap else -1
            output[i] = min_size
        
        return output
            

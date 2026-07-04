class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(math.sqrt(x[0]**2+x[1]**2), x) for x in points]    # O(n)
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(list(heapq.heappop(heap)[1]))
        return res

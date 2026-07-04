class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _ in range(k):
            pair = heapq.heappop(heap)
            res.append(pair[1])
        return res
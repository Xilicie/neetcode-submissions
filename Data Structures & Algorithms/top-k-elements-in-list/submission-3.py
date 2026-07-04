class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        x = []
        heapq.heapify_max(x)

        for key, val in count.items():
            heapq.heappush_max(x, (val, key))

        res = []
        for _ in range(k):
            pair = heapq.heappop_max(x)
            res.append(pair[1])
        
        return res
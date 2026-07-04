class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket)-1, -1, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])


                k -= 1
                if k == 0:  
                    break
            if k == 0:  break
        return res
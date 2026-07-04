class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            s = target - num
            if s not in seen:
                seen[num] = index
                continue
            
            return [seen[s], index]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {nums[0]: 0}
        for i in range(1, len(nums)):
            t = target - nums[i]
            if t in seen:
                return [seen[t], i]
            
            seen[nums[i]] = i

            
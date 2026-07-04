class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}   # num : ind
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in seen:
                return [seen[num2], i]
            seen[nums[i]] = i
            
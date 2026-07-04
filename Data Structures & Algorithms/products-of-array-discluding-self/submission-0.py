class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * len(nums), [1] * len(nums)
        
        i, j = 1, len(nums) - 2
        while i < len(nums) and j > -1:
            prefix[i] = nums[i - 1] * prefix[i - 1]
            suffix[j] = nums[j + 1] * suffix[j + 1]
            i += 1
            j -= 1
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res
        

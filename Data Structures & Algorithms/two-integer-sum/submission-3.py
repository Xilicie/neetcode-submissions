class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                return [hash_map[target - nums[i]], i]

                
        


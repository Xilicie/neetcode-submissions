class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_nums = set(nums)
        return len(hash_nums) != len(nums)

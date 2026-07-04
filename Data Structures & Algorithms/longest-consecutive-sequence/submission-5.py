class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                streak = 1
                while num + 1 in nums:
                    streak += 1
                    num += 1
                if streak > longest:
                    longest = streak
        return longest



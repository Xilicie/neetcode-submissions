class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hash_map = {}   # value -> num of occurences
        if not nums:
            return 0
        streaks = []
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                longest = 1
                while num + 1 in nums:
                    longest += 1
                    num += 1
                streaks.append(longest)
        return max(streaks)



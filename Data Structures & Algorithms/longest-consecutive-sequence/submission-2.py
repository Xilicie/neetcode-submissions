class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [min(nums) - 1] + sorted(list(set(nums)))
        k = 0
        consec = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                k += 1
            else:
                consec.append(k)
                k = 1
        consec.append(k)
        return max(consec)


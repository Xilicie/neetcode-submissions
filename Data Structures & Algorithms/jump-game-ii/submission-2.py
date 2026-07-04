class Solution:
    def jump(self, nums: List[int]) -> int:
        L = R = 0
        jumps = 0

        while R < len(nums) - 1:
            farthest = L
            for i in range(L, R + 1):
                farthest = max(farthest, nums[i] + i)
            L = R + 1
            R = farthest

            jumps += 1
        
        return jumps
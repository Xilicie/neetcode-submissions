class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)

        nums1 = nums[:-1]
        nums2 = nums[1:]

        prev1_1 = prev1_2 = 0
        for num in nums1:
            temp = max(prev1_1 + num, prev1_2)
            prev1_1 = prev1_2
            prev1_2 = temp
        
        prev2_1 = prev2_2 = 0
        for num in nums2:
            temp = max(prev2_1 + num, prev2_2)
            prev2_1 = prev2_2
            prev2_2 = temp

        return max(prev1_2, prev2_2)
            
            
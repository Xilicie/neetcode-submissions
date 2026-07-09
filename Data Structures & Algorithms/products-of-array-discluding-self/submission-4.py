class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]] * len(nums)
        suf = [nums[-1]] * len(nums)

        # product of all numbers before the index and at index
        prod = nums[0]
        for i in range(1, len(nums)):
            prod *= nums[i]
            pre[i] = prod
        
        # product of all number after the index and at index
        prod = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            prod *= nums[i]
            suf[i] = prod
        

        output = [suf[1]] + [0] * (len(nums) - 2) + [pre[-2]]
        for i in range(1, len(nums)-1):
            output[i] = pre[i-1] * suf[i+1]
        
        return output
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(comb[:])
                return
            if i == len(nums) or cur_sum > target:
                return
            
            comb.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            comb.pop()
        
            backtrack(i + 1, cur_sum)

        backtrack(0, 0)
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # target time: O(n^2)
        # target space: O(1)

        nums.sort()

        res = []

        # i < j < k
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[i] == -(nums[j] + nums[k]):
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    k -= 1
                elif nums[i] < -(nums[j] + nums[k]):
                    j += 1
                else:
                    k -= 1
        return res
            
        


                

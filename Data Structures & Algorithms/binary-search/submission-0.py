class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(target, start, end):
            if start > end:
                return -1
            
            middle = (start + end) // 2
            
            if nums[middle] == target:
                return middle
            
            elif nums[middle] > target:
                return find(target, start, middle - 1)
            
            else:
                return find(target, middle + 1, end)
            
        return find(target, 0, len(nums) - 1)
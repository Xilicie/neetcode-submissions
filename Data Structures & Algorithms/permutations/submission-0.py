class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def bt():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    bt()
                    path.pop()
        bt()
        return res

                    
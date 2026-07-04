class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        def volume(l, r):
            return min(heights[l], heights[r]) * (r - l)

        cur_vol = volume(l, r)

        while l < r:
            if cur_vol < volume(l, r):
                cur_vol = volume(l, r)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
            
            
        return cur_vol

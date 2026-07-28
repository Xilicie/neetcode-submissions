class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0

        i, j = 0, len(heights)-1
        while i < j:
            cur_vol = (j - i) * min(heights[i], heights[j])
            max_vol = max(max_vol, cur_vol)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_vol
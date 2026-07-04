class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        volume = 0
        
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                volume += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                volume += maxRight - height[r]
        return volume



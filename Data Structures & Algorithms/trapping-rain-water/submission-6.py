class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = [0] * len(height), [0] * len(height)
        lmax, rmax = height[l], height[r]
        
        for i in range(1, len(height)):
            maxLeft[i] = lmax
            if height[i] > lmax:
                lmax = height[i]
            
        for j in range(len(height) - 2, -1, -1):
            maxRight[j] = rmax
            if height[j] > rmax:
                rmax = height[j]
        volume = 0
        for k in range(len(height)):
            if min(maxLeft[k], maxRight[k]) < height[k]:
                continue
            volume += min(maxLeft[k], maxRight[k]) - height[k]
        return volume



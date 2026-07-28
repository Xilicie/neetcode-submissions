class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        # prefix max
        pre_max = 0
        for i in range(1, n):
            pre_max = max(height[i - 1], pre_max)
            prefix[i] = pre_max
        
        # suffix max
        suf_max = 0
        for i in range(n - 2, -1, -1):
            suf_max = max(height[i + 1], suf_max)
            suffix[i] = suf_max
        
        total_vol = 0
        for i in range(1, n - 1):
            volume = min(prefix[i], suffix[i]) - height[i]
            total_vol += max(0, volume)
        
        return total_vol
            
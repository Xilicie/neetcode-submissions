class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window = {}
        longst = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            while window and (r - l + 1) - max(window.values()) > k:
                window[s[l]] = window.get(s[l]) - 1
                l += 1
            longst = max(longst, r - l + 1)
        return longst


            
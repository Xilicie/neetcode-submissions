class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        elif len(s) < 2:
            return 1
        l, r = 0, 1
        seen, maxL = set(), 1

        seen.add(s[l])
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxL = max(len(seen), maxL)
            r += 1
        return maxL
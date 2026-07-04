class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        
        mapT = Counter(t)   # keeps track of chars of t        
        window = {}         # sliding window, expands to the right, shrinks from left
        formed = 0          # how many chars met their count
        substr = ""         # min substring
        minLen = float('infinity')
        l = 0               # left pointer

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            minLen += 1

            if s[r] in mapT and window[s[r]] == mapT[s[r]]:
                formed += 1
            
            while formed == len(mapT) and l <= r:
                if (r - l + 1) < minLen:
                        minLen = r - l + 1
                        substr = s[l:r + 1]
                window[s[l]] -= 1
                 
                if s[l] in mapT and window[s[l]] < mapT[s[l]]:
                    formed -= 1
                    
                l += 1
        return substr


                
        




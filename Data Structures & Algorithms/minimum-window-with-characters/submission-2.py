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
            c = s[r]
            window[c] = window.get(c, 0) + 1
            minLen += 1

            if s[r] in mapT and window[c] == mapT[c]:
                formed += 1
            
            while formed == len(mapT) and l <= r:
                c = s[l]
                if (r - l + 1) < minLen:
                        minLen = r - l + 1
                        substr = s[l:r + 1]
                window[c] -= 1
                 
                if c in mapT and window[c] < mapT[c]:
                    formed -= 1
                    
                l += 1
        return substr


                
        




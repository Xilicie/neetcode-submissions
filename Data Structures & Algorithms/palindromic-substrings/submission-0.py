class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def palindrome_1(i):
            p = 1
            l, r = i - 1, i + 1
            while (
                l >= 0 and r < n and
                s[l] == s[r]
            ):
                p += 1
                l -= 1
                r += 1
            return p
        
        def palindrome_2(i):
            p = 1
            l, r = i - 1, i + 2
            while (
                l >= 0 and r < n and
                s[l] == s[r]
            ): 
                p += 1
                l -= 1
                r += 1

            return p

        res = 0
        for i in range(n):
            res += palindrome_1(i)
            if i + 1 < n and s[i] == s[i + 1]:
                res += palindrome_2(i)
            
        return res


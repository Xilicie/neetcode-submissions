class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0

        def oddLenPalindrome(i):
            l = r = i
            palindrome = s[i]
            while l - 1 >= 0 and r + 1 < len(s) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
                palindrome = s[l:r+1]
                
            return palindrome

        def evenLenPalindrome(i):
            l = i
            r = i + 1
            palindrome = s[i:i+2]
            while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
                palindrome = s[l:r+1]
                
            return palindrome




        for i in range(len(s)):
            # odd-length palindrome
            odd_palindrome = oddLenPalindrome(i)
            if len(odd_palindrome) > resLen:
                res = odd_palindrome
                resLen = len(odd_palindrome)

            # even-length palindrome
            if i + 1 != len(s) and s[i] == s[i + 1]:
                even_palindrome = evenLenPalindrome(i)
                if len(even_palindrome) > resLen:
                    res = even_palindrome
                    resLen = len(even_palindrome)

        


        return res

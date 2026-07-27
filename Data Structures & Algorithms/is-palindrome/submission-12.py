class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(s)
        l = 0 
        r = len(new_s)-1

        while l <= r:
            while l < r and not new_s[l].isalnum():
                l += 1
            while l < r and not new_s[r].isalnum():
                r -= 1

            if new_s[l].lower() != new_s[r].lower():
                return False

            l += 1
            r -= 1

        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabetS = [0] * 26
        alphabetT = [0] * 26
        for i in range(len(s)):
            alphabetS[ord(s[i]) - ord('a')] += 1
            alphabetT[ord(t[i]) - ord('a')] += 1
        return alphabetS == alphabetT


        
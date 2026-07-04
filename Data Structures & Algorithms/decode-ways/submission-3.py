class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * 3
        for i in range(len(s)-1, -1, -1):
            dp = [0] + dp[:2]
            if s[i] == '0':
                dp[0] = 0
            else:
                dp[0] = dp[1]

            if (i + 1 < len(s) and
                (s[i] == '1' or 
                s[i] == '2' and s[i + 1] in '0123456')):
                dp[0] += dp[2]
            
        return dp[0]
# June10 2020
#DP
# TODO
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp solution
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        for l in range(1,n):
            for i in range(n-l):
                j = i + l
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
        return dp[0][-1]
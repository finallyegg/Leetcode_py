# June 10 2020
# DP on string

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ret = 0
        
        for i in range(n):
            dp[i][i] = 1
            
        # dp[i][j] indicate from i to j forms palindromic
        
        for l in range(1,n):
            for i in range(n-l):
                j = i + l
                if s[i] == s[j] and (dp[i+1][j-1] or (j-i) == 1):
                    dp[i][j] = 1
                    ret+=1
        
        ret+=n
        return ret
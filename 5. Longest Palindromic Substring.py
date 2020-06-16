#dp
#TODO manacher's 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        m = 1
        st = 0
        
        for l in range(1,n):
            for i in range(n-l):
                j = i + l
                if s[i] == s[j] and (dp[i+1][j-1] or (j-i) == 1):
                    dp[i][j] = 1
                    
                    if j-i+1 > m:
                        m = j-i+1
                        st = i
        
        return s[st:st+m]
    
    
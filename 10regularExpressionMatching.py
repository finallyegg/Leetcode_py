class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s)==0
        match = (len(s)>0) and (s[0] == p[0] or p[0] == '.')

        if (len(p)>=2) and p[1] == '*':
            return Solution.isMatch(self,s,p[2:]) or (match and Solution.isMatch(self,s[1:],p))
        else:
            return match and Solution.isMatch(self,s[1:],p[1:])
   
    def isMatchDP(self, s: str, p: str) -> bool:
        pn = len(p)
        sn = len(s)
        dp = [[False for x in range(sn+1)] for y in range(pn+1)]
        dp[pn][sn] = True
        for i in range(pn-1,-1,-1):
            for j in range(sn-1,-1,-1):
                if i == pn and j == sn:
                    continue
                match = s[j] == p[i] or p[i] == '.'
                if i+1<pn and p[i+1]=='*':
                    dp[i][j] = dp[i+2][j] or (match and dp[i][j+1])
                else:
                    dp[i][j] = match and dp[i+1][j+1]
        return dp[0][0]        

print(Solution.isMatch(Solution,"aa","a*"))
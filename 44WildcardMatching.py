class Solution:
    def isMatchR(self, s: str, p: str) -> bool:
        if len(p)==0:
            return len(s)==0
        if len(s)==0:
            if len(p) == 0:
                return True
            elif p[0]!='*':
                return False
            else:
                return Solution.isMatch(self,s,p[1:])
        else:
            firstMatch = (s[0] == p[0]) or (p[0] == '?')
            if p[0] == '*':
                return Solution.isMatch(self,s[1:],p) or Solution.isMatch(self,s,p[1:])
            else:
                return firstMatch and Solution.isMatch(self,s[1:],p[1:])

    def isMatch(self, s:str, p:str) -> bool:
        pn = len(p)
        sn = len(s)
        if not s:
            if not p:
                return True
            for i in range(pn):
                if p[i]!='*':
                    return False
            return True
        dp = [[False for x in range(sn+1)]for y in range(pn+1)]
        dp[pn][sn]=True
        for y in range(pn,-1,-1):
            for x in range(sn,-1,-1):
                if y==pn and x ==sn:
                    continue
                firstMatch = y<pn and x<sn and (p[y]==s[x] or p[y]=='*' or p[y] == '?')
                if y < pn and p[y] == '*':
                    dp[y][x] = dp[y+1][x] or (dp[y][x+1] and firstMatch)
                else:
                    dp[y][x] = firstMatch and dp[y+1][x+1]
        return dp[0][0]
# print(Solution.isMatch(Solution,"","?"))
print(Solution.isMatch(Solution,"ssab","s*"))
# print(Solution.isMatch(Solution,"miss","m??*ss"))

# print(Solution.isMatch(Solution,"mississippi","m??*ss*?i*pi"))
# print(Solution.isMatch(Solution,"a","a*"))
# print(Solution.isMatch(Solution,"adceb","*a*b"))
# print(Solution.isMatch(Solution,"acdcb","a*c?b"))
# print(Solution.isMatch(Solution,"aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab","*ab***ba**b*b*aaab*b"))
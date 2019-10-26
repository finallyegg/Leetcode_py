class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for i in range(len(s))]
        max = -1
        for i in range(len(s)):
            if s[i] == '(':
                dp[i] = 0
            else:
                if i>0 and s[i-1] == '(':
                    dp[i]=2
                    if i > 2:
                        dp[i]+=dp[i-2]
                    if dp[i] > max:
                        max = dp[i]
                if s[i-1] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1]=='(':
                    dp[i] = dp[i-1]+2
                    if i-dp[i-1]-1 > 0:
                        dp[i]+=dp[i-dp[i-1]-2]
                    if dp[i] > max:
                        max = dp[i]
                
        return max

print(Solution.longestValidParentheses(Solution,"(()))())("))
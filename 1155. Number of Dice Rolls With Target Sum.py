# June 8 2020
#DP 
# Logic
# TODO

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for j in range(d+1)]

        dp[0][0] = 1
        for i in range(1,d+1):
            for j in range(1,target+1):
                for k in range(1,f+1):
                    if j - k >= 0:
                        dp[i][j] += dp[i-1][j-k]
                        

        return dp[d][target]

a = Solution()
print(a.numRollsToTarget(2,6,7))
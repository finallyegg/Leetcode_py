class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for x in range(m+1)]for y in range(n+1)]
        for y in range(n,-1,-1):
            for x in range(m,-1,-1):
                if y< n-1 and x< m-1:
                    dp[y][x] = dp[y+1][x] + dp[y][x+1]
        return dp[0][0]

print(Solution.uniquePaths(Solution,7,3))
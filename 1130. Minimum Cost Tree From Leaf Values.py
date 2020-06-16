# TODO stack O(N)
# DP

from typing import List
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        # l is the length of sub array from i to j
        # k is an item where i <= k < j
        for l in range(2,n+1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i,j):
                    rootval = max(arr[i:k+1]) * max(arr[k+1:j+1])
                    o1 = dp[i][k]
                    o2 = dp[k + 1][j]
                    dp[i][j] = min(dp[i][j], rootval + dp[i][k] + dp[k + 1][j])
        return dp[0][-1]

a = Solution()
l = [6,2,4,8]
print(a.mctFromLeafValues(l))

# TODO
class Solution:
    # Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

    # Intuition: the unique bst of i ( 0 <= i <= n) is left unique * right unique
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]
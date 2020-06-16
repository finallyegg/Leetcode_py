# June 6
# DP
from typing import List
import sys

class Solution:
    # divide change into smaller amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i - j] + 1,dp[i]) #TODO
                    
        return (dp[amount] if dp[amount] != sys.maxsize else -1)

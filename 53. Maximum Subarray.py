# TODO
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # Gridfly doesnot work, think how to solve the transition function
        # n = len(nums)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = nums[i]
        # for l in range(1,n):
        #     for i in range(n-l):
        #         j = i + l
        #         side =max(dp[i][j-1] , dp[i+1][j])
        #         combine = side - dp[i+1][j-1]
        #         dp[i][j] = max(side,combine)

        # Solution
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        m = dp[0]
        for i in range(1, n):
            dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i]
            m = max(dp[i], m)
        return m

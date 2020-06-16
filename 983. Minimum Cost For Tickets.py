#June 6 2020
# DP

from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0 for i in range(days[-1]+1)]
        
        # dp[i] = cost[i] + dp[days without coverage]
        
        for day in range(1,len(dp)):
            if day not in days:
                dp[day] = dp[day-1] # trivial days
            else:
                o1 = dp[max(day-1,0)] + costs[0]
                o2 = dp[max(day-7,0)] + costs[1]
                o3 = dp[max(day-30,0)] + costs[2]
                dp[day] = min(o1,o2,o3)
        return dp[-1]
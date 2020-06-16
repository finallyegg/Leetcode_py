class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 1 or len(prices) == 0:
#             return 0
#         n = len(prices)
        
#         dp = [0 for _ in range(n)] 
        
#         for l in range(1,n):
#             for i in range(n-l):
#                 j = i + l 
#                 trade = max(0,prices[j]-prices[i])
#                 dp[i]= max(trade, max(dp[i],dp[i+1]))
#         # But this cost toooooo much space, save space using one row      
#         return dp[0]
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        profit = 0
        for i in prices:
            minprice = min(minprice,i)
            profit = max(i-minprice , profit)
        
        return profit
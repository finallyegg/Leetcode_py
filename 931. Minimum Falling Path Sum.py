# Jun 6 2020
# DP 

from typing import List
import sys
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        
        for i in range(n):
            for j in range(n):
                if i == 0:
                    continue
                o1 = (A[i-1][j-1] if j-1 >= 0 else sys.maxsize)
                o2 = A[i-1][j]
                o3 = (A[i-1][j+1] if j+1 < n else sys.maxsize)
                
                A[i][j] = min(o1,o2,o3) + A[i][j]
        return min(A[n-1])

a = Solution()
b = [[-19,57],[-40,-5]]
a.minFallingPathSum(b)
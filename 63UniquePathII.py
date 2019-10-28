class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if not obstacleGrid:
            return 0
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    continue
                elif i==n-1 and j == m-1 :
                    obstacleGrid[i][j]= -1
                else:
                    if j < m-1 and obstacleGrid[i][j+1] != 1:
                        obstacleGrid[i][j] += obstacleGrid[i][j+1]
                    if i < n-1 and obstacleGrid[i+1][j] != 1:
                        obstacleGrid[i][j] += obstacleGrid[i+1][j]
        return max(-obstacleGrid[0][0],0)

print(Solution.uniquePathsWithObstacles(Solution,[[0,0,0],[0,1,0],[0,0,0]]))
# print(Solution.uniquePathsWithObstacles(Solution,[[1]]))
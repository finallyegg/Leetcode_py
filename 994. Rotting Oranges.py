# May 28 2020
# TODO: Optimaized
from typing import List
import queue
class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = queue.Queue()
        rotten = 0

        time = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    q.put([row,col,0])
                elif grid[row][col] == 1:
                    rotten += 1

        while not q.empty():
            a = q.get()
            row = a[0]; col = a[1]; step = a[2]
            if(grid[row][col] == 2 and step != 0):
                continue
            
            step += 1
            grid[row][col] = 2
            rotten -= 1
            # step = time + 1
            if row > 0 and grid[row-1][col] == 1:
                q.put([row-1,col,step])
            if row + 1 < len(grid) and grid[row + 1][col] == 1:
                q.put([row+1,col,step])
            if col > 0 and grid[row][col - 1] == 1:
                q.put([row,col - 1,step])
            if col + 1 < len(grid[0]) and grid[row][col+1] == 1:
                q.put([row,col + 1,step])

            time = max(time,step - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1
            
        return time


a = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid1 = [[2,1,1],[0,1,1],[1,0,1]]
grid2 = [[0,2]]
grid3 = [[2],[1],[1],[1],[2],[1],[1]]
print(a.orangesRotting(grid3))
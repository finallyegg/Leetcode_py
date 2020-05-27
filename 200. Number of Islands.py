# May 27 2020
# BFS

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def DFS(row: int,col: int, grid: List[List[str]]):
            if (row >= len(grid) or row < 0 or col >=len(grid[0]) or col < 0):
                return 
            if grid[row][col] == "1":
                grid[row][col] = 0
                DFS(row+1,col,grid) #south
                DFS(row,col+1,grid) #east
                DFS(row,col-1,grid) #west
                DFS(row-1,col,grid) #north
            else:
                return  # BaseCase

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    DFS(row,col,grid)
        return count
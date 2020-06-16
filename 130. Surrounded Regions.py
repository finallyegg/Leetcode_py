#June 02 2020

#DFS
from typing import List

class Solution:
    def DFS(self,i,j,board):
        board[i][j] = 'E'
        if (i+1) < len(board) and board[i+1][j] == 'O':
            self.DFS(i+1,j,board)
        if (i-1) >= 0 and board[i-1][j] == 'O':
            self.DFS(i-1,j,board)
        if (j+1) < len(board[i]) and board[i][j+1] == 'O':
            self.DFS(i,j+1,board)
        if (j-1) >= 0 and board[i][j-1] == 'O':
            self.DFS(i,j-1,board)
        return 
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for i in range(len(board)):
            for j in range(len(board[i])): 
                if (i == 0 or j == 0 or i == len(board)-1 or j == len(board[i])-1) and board[i][j] == 'O':
                        self.DFS(i,j,board)
        print(board)   
        for i in range(len(board)):
            for j in range(len(board[i])):        
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board
                   
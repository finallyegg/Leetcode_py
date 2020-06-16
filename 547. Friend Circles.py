# June 2 2020

from typing import List
# Union Find 
class Solution:
    def find(self,parent_array, i):
        if parent_array[i] == -1:
            return i
        else:
            return self.find(parent_array,parent_array[i])
    def findCircleNum(self, M: List[List[int]]) -> int:

        parent = [-1] * (len(M))
        
        for row in range(len(M)):
            for col in range(row+1,len(M[row])):
                if M[row][col] == 1:
                    # Find
                    x = self.find(parent,row) # x is the subset of row
                    y = self.find(parent,col) # y is the subset of col
                    if x != y:
                        # Union
                        parent[x] = y
                        
        count = 0
        for i in parent:
            if i == -1:
                count += 1
        return count
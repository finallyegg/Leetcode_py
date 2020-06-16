# June 02 2020
# Union Find 

from typing import List
class Solution:
    def find(self,parent_array,i):
        if parent_array[i] == -1:
            return i
        else:
            return self.find(parent_array,parent_array[i])

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        count = -1
        
        for edge in edges:
            x = edge[0]
            y = edge[1]
            count = max(x,count)
            count = max(y,count)
        
        parent_array = [-1] * (count+1)
        
        for edge in edges:
            x = edge[0]
            y = edge[1]
            x_parent = self.find(parent_array,x)
            y_parent = self.find(parent_array,y)

            if x_parent == y_parent:
                return [x,y]
            parent_array[x_parent] = y_parent
        

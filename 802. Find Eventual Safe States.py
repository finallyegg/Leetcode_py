# June 02 2020

#BFS find cycle
from typing import List

# when use color to print subtree
# 0 is unvisit, 1 is safe and 2 is unsafe
class Solution:
    def DFS(self,i,graph,color):
        if color[i] != 0:
            return color[i] == 1

        color[i] = 2
        for node in graph[i]:
            if not self.DFS(node,graph,color):
                return False
        color[i] = 1
        return True
            
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        res = []
        for i in range(len(graph)):
            if self.DFS(i,graph,color):
                res.append(i)
        return res
            
        
a = Solution()
l = [[1,2,3,4],[1,2,3,4],[3,4],[4],[]]
print(a.eventualSafeNodes(l))
# May 27 2020

# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. 
# Any server can reach any other server directly or indirectly through the network.
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
# Return all critical connections in the network in any order.

from typing import List
class Solution:
    time = 0
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # treat all as direct graph
        # make discovery and low list respectively
        # node: 0, 1, 2, 3
        # disc: 1, 2, 4, 3
        # low:  1, 1, 1, 3

        # construct direct edge list
        edge = dict()
        discovered_stack = []
        disc = [-1] * n
        low = [-1] * n
        
        for i in range(len(connections)):
            if connections[i][0] not in edge:
                edge[connections[i][0]] = set()
            edge[connections[i][0]].add(connections[i][1])

            if connections[i][1] not in edge:
                edge[connections[i][1]] = set()
            edge[connections[i][1]].add(connections[i][0])

        def DFS(node_index,previous_index):
            # core: construct disc and low array
            self.time += 1
            disc[node_index] = self.time
            low[node_index] = disc[node_index]

            for ancestor in edge[node_index]:
                if ancestor == previous_index:
                    continue   # keep every edge one-way
                
                if disc[ancestor] == -1:
                    DFS(ancestor,node_index) #core
                    low[node_index] = min(low[node_index],low[ancestor]) # core
                else:
                    low[node_index] = min(low[node_index],disc[ancestor]) #core
            
                if low[ancestor] > disc[node_index]: # core
                    discovered_stack.append([node_index,ancestor])
        
        for i in range(n):
            if disc[i] == -1:
                DFS(i,-1)
            
        # print(low)
        # print(disc)
        return discovered_stack
4
r = [[0,1],[1,2],[2,0],[1,3]]

l = [[1,0],[2,1],[3,2],[4,2],[4,3],[3,0],[4,0]]
a = Solution()
print(a.criticalConnections(5,l))

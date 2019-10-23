import collections
import heapq
def productExceptSelf( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [0]*len(nums)
        r = [0]*len(nums) 
        out = [0]*len(nums)

        l[0] = 1
        r[len(nums)-1] = 1
        for i in range(1,len(nums)):
            l[i] = l[i-1]*nums[i-1]
        for i in reversed(range(len(nums)-1)):
            r[i] = r[i+1]*nums[i+1]

        for i in range(0,len(nums)):
            out[i] = l[i]*r[i]
        return out

def findMinHeightTrees(n, edges):
        g = collections.defaultdict(set)
        for i in edges:
            g[i[0]].add(i[1])
            g[i[1]].add(i[0])
        
        minDepth = 99999
        out = []
        for i in g:
            q = [(i,0)]
            maxdepth = -1
            visited = set()
            while q:
                node, depth = heapq.heappop(q)
                maxdepth = max(maxdepth,depth)
                visited.add(node)
                for j in g[node]:
                    if j not in visited:
                        q.append((j,depth+1))
            if maxdepth<minDepth:
                minDepth = maxdepth
                out *= 0 
                out.append(i)
            elif maxdepth==minDepth:
                out.append(i)
        return out

def findMinHeightTrees1(n, edges):
        g = collections.defaultdict(set)
        for i in edges:
            g[i[0]].add(i[1])
            g[i[1]].add(i[0])
        
        leaves = [i for i in range(n) if len(g[i])==1]
        while n > 2:
            # cut all leaves
            n-= len(leaves)
            newleaves = []
            for i in leaves:
                j = g[i].pop()
                g[j].remove(i)
                if len(g[j])==1:
                    newleaves.append(j)
            leaves = newleaves
        return leaves

# print(findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
print(findMinHeightTrees1(12,[[0,1],[0,2],[0,3],[3,4],[3,5],[1,6],[4,7],[2,8],[0,9],[0,10],[2,11]]))
import queue as Queue
import collections
import numpy as np
import heapq
import sys
def findCheapestPrice1(n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    # construct graph matrix
    graph_g = [[]for i in range(n)]
    for i in flights:
        ori = i[0]
        dest = i[1]
        dura = i[2]
        graph_g[ori].append((dest,dura))
        # graph_g[dest][ori] = dura 
    distance = [99999999]*n
    distance[src] = 0
    s = []
    q = Queue.PriorityQueue(n)
    q.put((0,src,0))
    while not q.empty():
        
        
        elem = q.get()
        
        v = elem[1]
        w = elem[0]
        depth = elem[2]
        s.append((v,w))
        # update nearby's distance
        
        for index in range(0,len(graph_g[v])):
            dest_t = graph_g[v][index][0]
            dura_t = graph_g[v][index][1]
            if(depth==K and dest_t==dst ):
                if((distance[v]+dura_t)<distance[dest_t]):
                    distance[dest_t] = distance[v]+dura_t
                    q.put((distance[v],dest_t,depth+1))
            if(depth<K ):
                if((distance[v]+dura_t)<distance[dest_t]):
                    distance[dest_t] = distance[v]+dura_t
                    q.put((distance[v],dest_t,depth+1))
                    
       
    result = int(distance[dst])
    if (result == 99999999):
        return -1
            
    return result

def findCheapestPrice(n, flights, src, dst, k):
    f = collections.defaultdict(dict)
    for a, b, p in flights:
        f[a][b] = p
    heap = [(0, src, k + 1)]
    while heap:
        p, i, k = heapq.heappop(heap)
        if i == dst:
            return p
        if k > 0:
            for j in f[i]:
                heapq.heappush(heap, (p + f[i][j], j, k - 1))
    return -1
# print(findCheapestPrice(17,[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]],13,4,130))

def networkDelayTime(times, N, K):
    """
    :type times: List[List[int]]
    :type N: int
    :type K: int
    :rtype: int
    """
    g = collections.defaultdict(dict)
    distance = {}
    for (b,e,w) in times:
        g[b][e] = w
    pq = [(0,K,0)]
    while pq:
        d,nodeIndex, depth = heapq.heappop(pq)
        if nodeIndex not in distance:
            distance[nodeIndex] = d
            for j in g[nodeIndex]:
                if j not in distance:
                    heapq.heappush(pq,(d+g[nodeIndex][j],j,depth+1)) 

    return max(distance.values()) if len(distance)==N else -1

# print(networkDelayTime([[1,2,1],[2,1,3]],2,2))
print(networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]],4,1))
# print(networkDelayTime([[1,2,1],[2,3,2],[1,3,4]],3,1))
# print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
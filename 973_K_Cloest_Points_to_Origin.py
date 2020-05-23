# May 21 2021
# TODO: divide and conqure

import math
from typing import List

class Solution:
# Normal solution, compute distance for all, and store them into a Array
    def distance(self, point:List[int]):
        return math.sqrt(point[0]**2 + point[1]**2)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distanceArray = []
        for i in range(len(points)):
            distanceArray.append((self.distance(points[i]),i))
        retVal = []

        distanceArray.sort(key=self.getKey)
        for j in range(K):
            retVal.append(points[distanceArray[j][1]])
        return retVal

    def getKey(self,pointTuple):
        return pointTuple[0]

#But we can do this in much simple code
class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # lambda here is like swift closure
        points.sort(key = lambda points: points[0]**2 + points[1]**2)
        return points[:K]

#But if we build a data structure, only allows K max instances at a time
# Run time analsis: NlogK
import heapq
class Solution3:
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # as always we create a min heap only hold K item at once
        heap = []
        for (x,y) in points:
            # reversed minqueue
            distance = -x**2 - y**2
            # check if heap is full
            if heap.count == K :
                heapq.heappushpop(heap, [distance,x,y])
            else:
                heapq.heappush(heap, [distance,x,y])
        return [(x,y) for (distance,x,y) in heap]

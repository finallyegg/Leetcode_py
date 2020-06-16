# June 5 2020
# TODO two pointer and DP

from queue import Queue
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # use stack to handle terrain 
        # new block keep popping until reach un
        stack = []
        cap = 0
        current_i = 0
        while current_i < len(height):
   
            while stack and height[stack[len(stack)-1]] < height[current_i]:
                p_i = stack.pop()
                if not stack:
                    break
                distance = current_i - stack[len(stack)-1] -1
                h = min(height[stack[len(stack)-1]], height[current_i]) - height[p_i]
                h = max(0,h)
                cap += distance * h
            stack.append(current_i)
            current_i += 1
        return cap

a = Solution()
b = [0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(b))
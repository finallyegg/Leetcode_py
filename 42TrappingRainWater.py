class Solution:
    def trap(self, height) -> int:
        s = []
        retval = 0
        if not height:return 0
        p = 0
        while p < len(height):
            while s and height[s[-1]] <= height[p]:
                waterHeight = height[s.pop()]
                if not s: break
                #compute waterVolume
                temp = min(height[p],height[s[-1]])
                retval+=(temp-waterHeight) * (p-s[-1]-1)
            s.append(p)
            p+=1
        return retval
#use stack to get the water by height level(not lateral level)
# print(Solution.trap(Solution,[2,1,0,2]))
print(Solution.trap(Solution,[0,1,0,2,1,0,1,3,2,1,2,1]))
        
        
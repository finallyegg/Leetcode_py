from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can treat the muiltiply as a muiltiply with two parts
        # left is a growing and right is a shrinking 
        l = [1] * (len(nums))
        r = [1] * (len(nums))

        for i in range(1,len(nums)):
            l[i] = nums[i-1] * l[i-1]
           
        for i in reversed(range(len(nums)-1)):
            r[i] = nums[i+1] * r[i+1]

        return [l[i] * r[i] for i in range(len(nums))]
        # complexcity: O(n)
        # Space O(n)

    #     1,2,3,4
    # l:  1,1,2,6
    # r:  24,12,4,1
    def productExceptSelf_SaveSpace(self, nums: List[int]) -> List[int]:
        # process of generate r array can be save
        l = [1] * (len(nums))
        for i in range(1,len(nums)):
            l[i] = nums[i-1] * l[i-1]
        r = 1
        for i in reversed(range(len(nums)-1)):
            r = r*nums[i+1]
            l[i] = l[i] * r
        return l
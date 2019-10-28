class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        retval = []
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            target = 0 - nums[i]
            lo = i+1
            high = len(nums)-1
            while lo < high:
                if nums[lo]+nums[high] == target:
                    retval.append([nums[i],nums[lo],nums[high]])
                    while lo+1 < len(nums) and nums[lo] == nums[lo+1]:
                        lo+=1
                    while high-1 > 0 and nums[high] == nums[high-1]:
                        high-=1
                if nums[lo]+nums[high] < target:
                    lo+=1
                else:
                    high-=1
        return retval 

print(Solution.threeSum(Solution,[-2,0,1,1,2]))
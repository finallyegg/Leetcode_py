class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        retval = 99999
        s = 0
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                tempSum = nums[i] + nums[l] + nums[r]
                diff = abs(tempSum - target)
                if diff < retval:
                    retval = diff
                    s = tempSum
                if tempSum == target:
                    return tempSum
                if tempSum > target:
                    r -=1
                if tempSum < target:
                    l +=1
                
        return s
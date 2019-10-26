class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        retval = [-1 for x in range(n+1)]
        for i in range(n):
            if 0<=nums[i]<=n:
                retval[nums[i]-1] = nums[i]
                

        for i in range(len(retval)):
            if retval[i]!=i+1:
                return i+1
        print(retval)
        return retval[-1]+1

print(Solution.firstMissingPositive(Solution,[]))
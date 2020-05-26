# May 26 2021

from typing import List

class Solution:
    # Brute Force
    def subarraySum(self, nums: List[int], k: int) -> int:
        # consider every subarray
        # Input:nums = [1,1,1], k = 2
        # output = 2
        count = 0
        for start in range(len(nums)):
            sumall = 0
            for end in range(start, len(nums)):
                sumall += nums[end]
                if sumall == k:
                    count += 1
        return count
        
    #Hashmap: [3,4,7,2,-3,1,4,2]
    # if index i and j at z spot have same sum, then the sum between i and j is 0
    # put (sum, occurance) in dict
    def subarraySum_optimal(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0
        mapp = dict()
        mapp[0] = 1
        for i in range(len(nums)):
            summ += nums[i]
            # if k = 0, then is the same case above
            if summ - k in mapp:
                count += mapp[summ - k]
            mapp[summ] = mapp.get(summ,0) + 1
        return count
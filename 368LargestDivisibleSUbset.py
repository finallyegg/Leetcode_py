#1,2,32%4
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        S = {-1:set()}
        for num in sorted(nums):
            S[num] = max((S[d] for d in S if num % d == 0), key=len) | {num}
        return list(max(S.values(),key=len))

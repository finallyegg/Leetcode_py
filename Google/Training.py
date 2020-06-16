# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6
from typing import List

class Solution:
    def minTrain(self,N:int,P:int,S:List[int]):
        S.sort(reverse=True)
        total_hour = float('inf')
        sum_array = [0 for _ in range(len(S)-P+1)]
        sum_array[0] = sum(S[0:0+P])
        for i in range(1,len(S)-P+1):
            sum_array[i] = sum_array[i-1] - S[i-1] + S[i+P-1]

        for i in range(len(S)-P+1):
            total_hour = min(total_hour,S[i] * P - sum_array[i])
        print(total_hour)

a = Solution()
a.minTrain(5,5,[7,7,1,7,7])
import collections
class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        l = 0
        count = 0
        while l < len(A):
            k = K
            r = l
            temp = set()
            while r < len(A):
                if k > 0:
                    if A[r] not in temp:
                        temp.add(A[r])
                        k-=1
                else:
                    if A[r] not in temp:
                        break
                if k == 0:
                    count+=1
                r+=1
                
            if r >= len(A) and k != 0:
                break
            l+=1
        return count

    def optimized(self,A,K:int):
        return help
    def helper(A,K):
        res = i = 0
        colle = collections.Counter()
        for j in range(len(K)):
            if colle[A[j]] == 0:
                colle[A[j]] += 1
                K -= 1
            while K < 0:
                colle[A[i]] -= 1
                if colle[A[i]] == 0:
                    K +=1
                i += 1
            res += r-i+ 1
        return res
A = [1,2,1,2,3]
K = 2
print(Solution.subarraysWithKDistinct(Solution,A,K))


class Solution(object):
    def minDistance_Using_Recurrsion(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)==len(word2)==0:
            return 0
        elif len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        x = Solution.minDistance(self,word1[:-1],word2)
        y = Solution.minDistance(self,word1,word2[:-1])
        z = Solution.minDistance(self,word1[:-1],word2[:-1])
        if word1[-1]!=word2[-1]:
            z+=1
        return min(x+1,y+1,z)

    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        if l1 ==l2==0:
            return 0
        elif l1 == 0:
            return l2
        elif l2 == 0:
            return l1
        ed = [[0 for x in range(l1+1)]for y in range(l2+1)]

        for i in range(l1+1):
            ed[0][i] = i
        for j in range(l2+1):
            ed[j][0] = j
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if word1[i-1]==word2[j-1]: #same as word[i] because of range we choose
                    ed[j][i] = min(ed[j][i-1]+1,ed[j-1][i]+1,ed[j-1][i-1])
                else:
                    ed[j][i] = min(ed[j][i-1]+1,ed[j-1][i]+1,ed[j-1][i-1]+1)
        return ed[l2][l1]
print(Solution.minDistance(Solution,"prosperity","properties"))
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = set(t)
        l=0
        r=0
        retval = (l,r)
        a = set()
        while r < len(s) and not t.issubset(a):
            a.add(s[r])
            r+=1
        if not t.issubset(a):
            return "" 
        retval = (l,r)
        length = r+1 - l
        while r < len(s):
            temp = set(s[l:r+1])
            if not t.issubset(temp):
                l+=1
                r+=1
            else:
                templ = r+1 - l
                if templ < length:
                    length = templ
                    retval = (l,r)
                l+=1
        return s[retval[0]:retval[1]+1]
            
            
print(Solution.minWindow(Solution,"ADOBECODEBANC","ABC"))            
print(Solution.minWindow(Solution,"a","aa"))            
#ADOBECODEBANC
#11
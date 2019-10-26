class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if n == 2:
            return x*x
        
        if n % 2 == 1:
            a =  Solution.myPow(self,x,n//2)
            return a*a*x
        else:
            a = Solution.myPow(self,x,n//2)
            return a*a

print(Solution.myPow(Solution,2,10))
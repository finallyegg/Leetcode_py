class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        retval = []
        if n == 1:
            return ["()"] #base case
        else:
            retval.append(Solution.generateParenthesis(Solution,n-1))
            retval.append(Solution.generateParenthesis(Solution,n-1))
            
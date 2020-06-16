# TODO
# May 28 2020

from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = 0; right = 0
        for i in s:
            if s[i] == '(':
                if right == 0:
                    left += 1
                else:
                    right -= 1
            elif s[i] == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1
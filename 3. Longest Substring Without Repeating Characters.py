# June 15

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        r = 0
        ret = 0
        for i in range(len(s)):
            r = i
            if s[i] not in d or d[s[i]] < l:
                ret = max(r-l+1, ret)
            else:
                while l < r and l <= d[s[i]]:
                    l += 1
            d[s[i]] = i
        return ret

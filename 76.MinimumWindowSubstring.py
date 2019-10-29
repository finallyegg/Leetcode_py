import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r = l
        retval = (l,r)
        a = []
        a.append(s[l])
        if not Solution.contains(a,t):
            r=l+1
            while r < len(s):
                a.append(s[r])
                if not Solution.contains(a,t):
                    r+=1
                else:
                    break
            if r == len(s):
                return "" 
        retval = (l,r)
        length = r+1 - l
        while r < len(s):
            temp = s[l:r+1]
            if not Solution.contains(temp,t):
                l+=1
                r+=1
            else:
                templ = r+1 - l
                if templ < length:
                    length = templ
                    retval = (l,r)
                l+=1
        return s[retval[0]:retval[1]+1]
    def contains(s,t):
        m = {}
        for i in t:
            if not i in m.keys():
                m[i] = 1
            else:
                m[i]+=1
        for i in s:
            if not i in m.keys():
                continue
            else:
                m[i]-=1
                if m[i] ==0:
                    del m[i]
        return not m

    def so(s,t):
        
        if not t or not s:
        return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]    
            
print(Solution.minWindow(Solution,"ADOBECODEBANC","ABC"))            
print(Solution.minWindow(Solution,"a","aa"))            
#ADOBECODEBANC
#11
print(Solution.minWindow(Solution,"ab","a"))            
print(Solution.minWindow(Solution,"a","a"))            

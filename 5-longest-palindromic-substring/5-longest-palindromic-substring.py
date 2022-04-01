class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        
        res = s[0]
        resLen = 0
        for c in range(len(s)):
            
            # if (c-1>=0 and c+1<len(s)) and (s[c-1] == s[c+1]):
            l = c-1
            r = c+1
            while (l>=0 and r<len(s)) and (s[l] == s[r]):
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            
            # elif (c+1<=len(s)-1) and (s[c]==s[c+1]):
            l = c
            r = c+1
            while (l>=0 and r<len(s)) and (s[l] == s[r]):
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        
        return res
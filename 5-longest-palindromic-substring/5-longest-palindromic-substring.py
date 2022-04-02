class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #odd case
        res = s[0]
        resLen = 0
        for c in range(len(s)):
            l = c-1
            r = c+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resLen<(r-l+1):
                    res = s[l:r+1]
                    resLen = r-l+1
                    
                l-=1
                r+=1
            
            l = c
            r = c+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resLen<(r-l+1):
                    res = s[l:r+1]
                    resLen = r-l+1
                    
                l-=1
                r+=1
            
        
        return res
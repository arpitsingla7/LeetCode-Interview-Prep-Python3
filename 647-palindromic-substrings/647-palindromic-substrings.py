class Solution:
    def countSubstrings(self, s: str) -> int:
        
        #odd case
        res = s[0]
        resLen = 0
        count = len(s)
        for c in range(len(s)):
            l = c-1
            r = c+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                if resLen<(r-l+1):
                    res = s[l:r+1]
                    resLen = r-l+1
                    
                l-=1
                r+=1
            
            l = c
            r = c+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                if resLen<(r-l+1):
                    res = s[l:r+1]
                    resLen = r-l+1
                    
                l-=1
                r+=1
            
        print(count)
        return count
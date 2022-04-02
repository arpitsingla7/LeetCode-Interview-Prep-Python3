class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        count = len(s)
        for c in range(len(s)):
            #odd case
            l = c-1
            r = c+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            
            #even case
            l = c
            r = c+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            
        return count
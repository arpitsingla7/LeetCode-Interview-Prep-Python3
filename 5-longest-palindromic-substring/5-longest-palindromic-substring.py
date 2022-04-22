class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        res = ""
        resLen = 0
        
        for i in range(0, len(s)):
            
            p1, p2 = i, i
            while p1>=0 and p2<len(s) and s[p1]==s[p2]:
                if (p2-p1+1)>resLen:
                    res = s[p1:p2+1]
                    resLen = p2-p1+1
                
                p1-=1
                p2+=1
                
                
            p1, p2 = i, i+1
            while p1>=0 and p2<len(s) and s[p1]==s[p2]:
                if (p2-p1+1)>resLen:
                    res = s[p1:p2+1]
                    resLen = p2-p1+1
                
                p1-=1
                p2+=1
        
        return res
        
        
                
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.res = s[0]
        self.resLen = 0
        def findres(l, r):
            while (l>=0 and r<len(s)) and (s[l] == s[r]):
                if (r-l+1)>self.resLen:
                    self.res = s[l:r+1]
                    self.resLen = r-l+1
                l-=1
                r+=1
            
            return self.res
        
        
        for c in range(len(s)):  
            odd = findres(c-1, c+1)
            even = findres(c, c+1)            
            result = odd if len(odd)>len(even) else even
        
        return result
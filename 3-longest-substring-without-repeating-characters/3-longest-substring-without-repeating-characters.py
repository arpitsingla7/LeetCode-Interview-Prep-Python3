class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        res = 0
        l = 0
        for r in range(0, len(s)):
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            
            charSet.add(s[r])
            res = max(res, len(charSet))
        
        return res
        
        
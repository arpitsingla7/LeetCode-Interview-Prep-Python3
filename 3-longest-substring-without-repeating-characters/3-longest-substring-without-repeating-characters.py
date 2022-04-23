class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        resLen = 0
        tempSet = set()
        l, r = 0, 0
        
        while r<len(s):
            while s[r] in tempSet:
                tempSet.remove(s[l])
                l+=1
            
            tempSet.add(s[r])
            resLen = max(resLen, r-l+1)
            r+=1
            
        
        return resLen
        
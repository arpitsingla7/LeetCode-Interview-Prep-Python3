class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charSet = set(s)
        count = 0
        for i in charSet:
            if s.count(i)!=t.count(i):
                return False
            else:
                count+=s.count(i)
            
        if count==len(t):
            return True
        return False
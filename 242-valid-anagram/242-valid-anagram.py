class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charSet = set(s)
        for i in charSet:
            if s.count(i)!=t.count(i):
                return False
            
        if len(s)==len(t):
            return True
        return False
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sCount = set(s)
        
        for i in sCount:
            if s.count(i)!=t.count(i):
                return False
        
        return True if len(s)==len(t) else False
                
            
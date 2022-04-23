class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s)!=len(t):
            return False
        
        charS = set(s)
        
        for ch in charS:
            if s.count(ch) != t.count(ch):
                return False
        
        return True
                
    
            
            
        
        
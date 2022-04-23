class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s)!=len(t):
            return False
        
        freqS = {}
        freqT = {}
        for ch in s:
            freqS[ch] = 1 + freqS.get(ch, 0)
        
        for ch in t:
            freqT[ch] = 1 + freqT.get(ch, 0)
            
        
        return freqS==freqT
    
            
            
        
        
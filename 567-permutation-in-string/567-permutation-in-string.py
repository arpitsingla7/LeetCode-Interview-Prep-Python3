class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2)<len(s1):
            return False
        
        s1Map = [0]*26
        s2Map = [0]*26
        for ch in range(len(s1)):
            s1Map[ord(s1[ch])-ord("a")]+=1
            s2Map[ord(s2[ch])-ord("a")]+=1
        
        if s1Map==s2Map:
            return True
        
        l, r = 0, len(s1)
        while r<len(s2):
            s2Map[ord(s2[l])-ord("a")] -=1
            s2Map[ord(s2[r])-ord("a")] +=1
            
            if s1Map==s2Map:
                return True
            l+=1
            r+=1
        
        return False
            
                
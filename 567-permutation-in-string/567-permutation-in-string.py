class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
        
        s1Map = [0]*26
        s2Map = [0]*26
        for i in range(len(s1)):
            s1Map[ord(s1[i])-ord("a")] +=1
            s2Map[ord(s2[i])-ord("a")] +=1
        
        if s2Map == s1Map:
            return True
        
        l=0
        for r in range(len(s1), len(s2)):
            s2Map[ord(s2[l])-ord("a")]-=1
            l+=1
            
            s2Map[ord(s2[r])-ord("a")]+=1
            
            if s2Map==s1Map:
                return True
        
        return False
            
        
        
            
            
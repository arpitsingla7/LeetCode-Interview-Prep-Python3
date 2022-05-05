class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s)<len(p):
            return []
        
        truth = [0]*26
        newTruth = [0]*26
        for i, ch in enumerate(p):
            truth[ord(ch)-ord("a")] += 1
            newTruth[ord(s[i])-ord("a")]+=1
        
        
        l, r = 0, len(p)
        res = [] 
        while r<=len(s):
            
            if newTruth==truth:
                res.append(l)
            
            if r<len(s):
                newTruth[ord(s[r])-ord("a")]+=1
                newTruth[ord(s[l])-ord("a")]-=1
            
            l+=1
            r+=1
        
        return res
        
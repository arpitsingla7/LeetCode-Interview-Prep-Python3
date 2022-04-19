class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashMap = {}
        
        for ind, c in enumerate(s):
            if c in hashMap:
                hashMap[c]= ind
                continue
            
            hashMap[c] = ind
            
            
        l = 0
        res = []
        while l<len(s):
            
            r = hashMap[s[l]]
            curSet = set(s[l:r+1])
            
            while curSet:
                tempSet = set()
                for c in curSet:
                    if hashMap[c]>r:
                        tempr = r
                        r = hashMap[c]
                        tempSet.update(set(s[tempr:r+1]))
                
                curSet = tempSet
                    
            res.append((r+1)-l)
            l = r+1
        
        return res
        
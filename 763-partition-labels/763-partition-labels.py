class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashMap = {}
        
        for ind, c in enumerate(s):
            if c in hashMap:
                hashMap[c][1] = ind
                continue
            
            hashMap[c] = [ind, ind]
            
            
        l = hashMap[s[0]][0]
        res = []
        while l<len(s):
            
            r = hashMap[s[l]][1]
            curSet = set(s[l:r+1])
            
            while curSet:
                tempSet = set()
                for c in curSet:
                    if hashMap[c][1]>r:
                        tempr = r
                        r = hashMap[c][1]
                        tempSet.update(set(s[tempr:r+1]))
                
                curSet = tempSet
                    
            res.append((r+1)-l)
            l = r+1
        
        return res
        
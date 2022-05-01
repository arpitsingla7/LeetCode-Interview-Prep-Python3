class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        res = []
        mapOps = ["+","C", "D"]
        for i in ops:
            
            if i not in mapOps:
                res.append(int(i))
            else:
                
                if i=="C":
                    res.pop()
                elif i=="D":
                    res.append(res[-1]*2)
                else:
                    res.append(res[-1] + res[-2])
        
        return sum(res)
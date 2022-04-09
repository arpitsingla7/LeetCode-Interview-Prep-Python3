class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        stack = [[temperatures[0], 0]]
        res = [0]*len(temperatures)
        
        for i in range(1, len(temperatures)):
            
            while stack and temperatures[i]>stack[-1][0]:
                ele, ind = stack.pop()
                res[ind] = i-ind
            
            stack.append([temperatures[i], i])
            
        return res
            
                
                
            
        
        
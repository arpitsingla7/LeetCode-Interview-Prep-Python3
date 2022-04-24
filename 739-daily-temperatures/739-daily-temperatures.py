class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            
        
            while stack and stack[-1][1]<temp:
                ind, val = stack.pop()
                res[ind] = i-ind
            
            stack.append([i, temp])
        
        return res
        
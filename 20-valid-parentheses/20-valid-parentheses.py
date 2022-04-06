class Solution:
    def isValid(self, s: str) -> bool:
        
        closeMap = {")": "(", "]":"[", "}":"{"}
        stack = []
        
        for bracket in s:
            
            if bracket not in closeMap:
                stack.append(bracket)
            else:
                if stack and stack[-1] == closeMap[bracket]:
                    stack.pop() 
                else:
                    return False
                
        return True if len(stack)==0 else False
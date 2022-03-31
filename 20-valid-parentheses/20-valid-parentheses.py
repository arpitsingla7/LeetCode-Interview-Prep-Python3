class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)==1:
            return False
        
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            
            if len(stack)!=0:
                if i == ")":
                    temp = stack.pop()
                    if temp + i != "()":
                        return False

                elif i == "]":
                    temp = stack.pop()
                    if temp + i != "[]":
                        return False

                elif i == "}":
                    temp = stack.pop()
                    if temp + i != "{}":
                        return False
            else:
                return False
            
        return True if len(stack)==0 else False
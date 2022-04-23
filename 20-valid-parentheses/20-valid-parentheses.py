class Solution:
    def isValid(self, s: str) -> bool:
        
        
        brackets = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for b in s:
            if b not in brackets:
                stack.append(b)
            else:
                if stack:
                    if brackets[b]==stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return False if stack else True
                
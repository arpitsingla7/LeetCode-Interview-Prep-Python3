class Solution:
    def isValid(self, s: str) -> bool:
        
        mapper = {")": "(" ,"]" : "[", "}": "{"}
        stack = []
        
        for b in s:
            if b not in mapper:
                stack.append(b)
            else:
                if stack and stack[-1]==mapper[b]:
                    stack.pop()
                else:
                    return False
            
        return True if len(stack)==0 else False
class Solution:
    def isValid(self, s: str) -> bool:
        
        mapper = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for bracket in s:
            if bracket not in mapper:
                stack.append(bracket)
                continue
            if len(stack)!=0:
                openBracket = stack.pop()
                if openBracket != mapper[bracket]:
                    return False
            else:
                return False
        
        return len(stack)==0
                
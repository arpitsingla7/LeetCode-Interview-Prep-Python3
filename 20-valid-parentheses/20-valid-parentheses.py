class Solution:
    def isValid(self, s: str) -> bool:
        
        mapper = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for bracket in s:
            if bracket not in mapper:
                stack.append(bracket)
                continue
            if stack and stack[-1]==mapper[bracket]:
                stack.pop()
            else:
                return False
        
        return len(stack)==0
                
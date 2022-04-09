class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = set(["+", "-", "/", "*"])
        stack = []
        
        for r in tokens:
            if r not in operators:
                stack.append(r)
            
            else:
                b = stack.pop()
                a = stack.pop()
    
                if r=="/":
                    # c = int(a)//int(b) if 
                    # c = c if c>0 else 0
                    c = int(int(a)/int(b))
                    stack.append(str(c))
                else:
                    stack.append(str(eval(a+r+b)))
        return int(stack[0])
        
        
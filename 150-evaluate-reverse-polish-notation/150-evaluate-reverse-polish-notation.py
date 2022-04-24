class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(t)
            
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if t == "/":
                    res = int(int(num1)/int(num2))
                    
                else:   
                    res = eval(num1+t+num2)
                      
                stack.append(str(res))
            
        return stack[0]
    
                
                
                
            
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a), len(b))):
            
            num1 = int(a[i]) if i<len(a) else 0
            num2 = int(b[i]) if i<len(b) else 0
            
            total = num1 + num2 + carry
            value = total%2
            res = str(value) + res
            carry = total//2
            
        
        if carry:
            res = "1"+res
        
        return res
        
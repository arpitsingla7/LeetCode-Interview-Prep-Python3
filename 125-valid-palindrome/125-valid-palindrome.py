class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        
        
        l, r = 0, len(s)-1
        
        while l<r:
            while l<r and not self.isalpha(s[l]):
                l+=1
            
            while l<r and not self.isalpha(s[r]):
                r-=1
                
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
            
        return True
    
        
    def isalpha(self, letter):
        if ((ord("A")<=ord(letter) and ord(letter)<=ord("Z")) 
           or (ord("a")<=ord(letter) and ord(letter)<=ord("z"))
           or (ord("0")<=ord(letter) and ord(letter)<=ord("9"))):
            return True
        return False
        
            
        
        
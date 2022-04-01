class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s)-1
        while l<r:
            while (l<r) and (s[l]==" " or not s[l].isalnum()):
                l+=1
                
            while (r>l) and (s[r] == " " or not s[r].isalnum()):
                r-=1
            
            ch1 = s[l].lower()
            ch2 = s[r].lower()
            if ch1 != ch2:
                return False
            l+=1
            r-=1
            
        return True
                
        
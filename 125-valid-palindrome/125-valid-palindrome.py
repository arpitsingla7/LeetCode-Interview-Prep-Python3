class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        sPali = ""
        
        for i in s:
            if i.isalnum():
                sPali+=i.lower()
        
        l, r = 0, len(sPali)-1
        
        while l<r:
            if sPali[l]!=sPali[r]:
                return False
            l+=1
            r-=1
        return True
        
        
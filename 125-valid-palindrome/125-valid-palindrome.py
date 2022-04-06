class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        sPali = ""
        
        for i in s:
            if i.isalnum():
                sPali+=i.lower()
        
        l, r = 0, len(sPali)
        
        return sPali[:] == sPali[::-1]
        
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letters = set(s)
        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        
        if len(t)==len(s):
            return True
        return False

        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        #check solution for capital letters 
        
        res = defaultdict(list)
        
        for word in strs:
            letters = [0]*26
            for ch in word:
                letters[ord(ch)-ord("a")] += 1
            
            res[tuple(letters)].append(word)
        
        return res.values()
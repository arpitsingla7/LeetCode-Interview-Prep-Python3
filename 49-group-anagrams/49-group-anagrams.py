class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        res = defaultdict(list)
        
        for word in strs:
            charList = [0]*26
            for ch in word:
                charList[ord(ch)-ord("a")]+=1
            
            res[tuple(charList)].append(word)
        
        return res.values()
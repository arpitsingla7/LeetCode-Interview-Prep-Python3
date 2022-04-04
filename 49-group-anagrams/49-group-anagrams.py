class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        res = defaultdict(list)
        
        for word in strs:
            charSet = [0]*26
            for s in word:
                charSet[ord(s)-ord("a")]+=1
                
            res[tuple(charSet)].append(word)
        
        return res.values()
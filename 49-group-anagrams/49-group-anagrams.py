class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        #method 1:
        res = defaultdict(list)
        
        for word in strs:
            sWord = sorted(word)
            sWord = "".join(sWord)
            if sWord in res:
                res[sWord].append(word)
                continue
            
            res[sWord].append(word)
            
        return res.values()
        
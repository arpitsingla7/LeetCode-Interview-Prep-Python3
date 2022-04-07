class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #method 2:
        res = defaultdict(list)
        
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord("a")] +=1
            res[tuple(count)].append(word)
        
        return res.values()
        
        
        
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
        
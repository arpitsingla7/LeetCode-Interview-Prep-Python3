class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Sol 1:
        res = defaultdict(list)
        
        for word in strs:
            sortedWord = "".join(sorted(word))
            res[sortedWord].append(word)
            
        return res.values()
            
        
        
        #Sol 2:
        res = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord("a")] +=1
                
            res[tuple(count)].append(s)
            
        return res.values()
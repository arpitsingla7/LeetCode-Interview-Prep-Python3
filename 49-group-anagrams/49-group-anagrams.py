class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #sort the words 
        
        
        #make a 26 letter arr
        wordMap = defaultdict(list)
        
        for s in strs:
            letters = [0]*26
            
            for ch in s:
                letters[ord(ch)-ord("a")] += 1
            
            wordMap[tuple(letters)].append(s)
        
        return wordMap.values()
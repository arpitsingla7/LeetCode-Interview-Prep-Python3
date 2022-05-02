class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(" ")
        if len(pattern)>len(words):
            return False
        
        #each pattern maps to different word
        hashMap = {}
        hashSet = set()
        for i, p in enumerate(pattern):
            if p in hashMap:
                if hashMap[p]!=words[i]:
                    return False
            else:
                if words[i] in hashSet:
                    return False
                
                hashMap[p] = words[i]
                hashSet.add(words[i])
        
        #that mapping is consistent 
        w = 0
        while w<len(words):
            m = w%len(pattern)
            
            if hashMap[pattern[m]]!=words[w]:
                return False
            w+=1
            
        return True if m==len(pattern)-1 else False
            
            
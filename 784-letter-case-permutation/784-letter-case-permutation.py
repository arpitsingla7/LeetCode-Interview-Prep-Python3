class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []
        substr = []
        
        def dfs(i):
            if i==len(s):
                copy = substr.copy()
                res.append("".join(copy))
                return 
            
            
            if s[i].isalpha():
                substr.append(s[i].lower())
                dfs(i+1)
                substr.pop()
                
                substr.append(s[i].upper())
                dfs(i+1)
                substr.pop()
            else:
                substr.append(s[i])
                dfs(i+1)
                substr.pop()
            
        
        dfs(0)
        return res
        
        

    
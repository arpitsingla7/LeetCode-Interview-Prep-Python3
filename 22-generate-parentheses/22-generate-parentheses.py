class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backTrack(remOpenBrackets, curOpenBrackets, s):
            if len(s)==(n*2):
                res.append(s)
                return 
            
            #if we can still add open brackets:
            if remOpenBrackets>0:
                backTrack(remOpenBrackets-1, curOpenBrackets+1, s+"(")
            
            if curOpenBrackets>0:
                backTrack(remOpenBrackets, curOpenBrackets-1, s+")")
                
    
        backTrack(n, 0, "")
        return res
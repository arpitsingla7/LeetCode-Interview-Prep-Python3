class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        res = []
        self.s = ""
        def backTrack(remOpenBrackets, curOpenBrackets):
            if len(self.s)==(n*2):
                res.append(self.s)
                return 
            
            #if we can still add open brackets:
            if remOpenBrackets>0:
                self.s+="("
                backTrack(remOpenBrackets-1, curOpenBrackets+1)
                self.s = self.s[:-1]
            #if we have open brackets that need closing brackets to complete 
            if curOpenBrackets>0:
                self.s+=")"
                backTrack(remOpenBrackets, curOpenBrackets-1)
                self.s = self.s[:-1]
    
        backTrack(n, 0)
        return res
        
        
        
        
        
        
        
#         res = []
        
#         def backTrack(remOpenBrackets, curOpenBrackets, s):
#             if len(s)==(n*2):
#                 res.append(s)
#                 return 
            
#             #if we can still add open brackets:
#             if remOpenBrackets>0:
#                 backTrack(remOpenBrackets-1, curOpenBrackets+1, s+"(")
            
#             #if we have open brackets that need closing brackets to complete 
#             if curOpenBrackets>0:
#                 backTrack(remOpenBrackets, curOpenBrackets-1, s+")")
                
    
#         backTrack(n, 0, "")
#         return res
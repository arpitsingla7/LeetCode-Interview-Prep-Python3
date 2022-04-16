class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []
        substr = []
        
        def dfs(i):
            if i==len(s):
                copy = substr.copy()
                res.append("".join(copy))
                return 
            
            substr.append(s[i].lower())
            dfs(i+1)
            substr.pop()
            if s[i].isalpha():
                
                substr.append(s[i].upper())
                dfs(i+1)
                substr.pop()
            # else:
            #     substr.append(s[i])
            #     dfs(i+1)
            #     substr.pop()
            
        
        dfs(0)
        return res
        
        
        
        
        
        
        
                
            
        
#         result = []
#         partial = []
#         S = s
#         def permHelper(index, partial):
            
#             if index==len(S):
#                 result.append(''.join(partial))
#                 return
            
#             if S[index].isalpha():
#                 partial.append(S[index].lower())
#                 permHelper(index+1, partial)
#                 partial.pop()
#                 partial.append(S[index].upper())
#                 permHelper(index+1, partial)
#                 partial.pop()
                
#             else:
#                 partial.append(S[index])
#                 permHelper(index+1, partial)
#                 partial.pop()

#         permHelper(0, partial)
#         return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         substr = []
#         s = s.lower()
#         def backTrack(i):
#             if i>=len(s):
#                 res.append("".join(substr.copy()))
#                 return 
            
#             #lower case
#             substr.append(s[i])
#             if s[i].isalpha():
#                 backTrack(i+1)
#                 substr.pop()
                
#                 #upper case
#                 substr.pop()
#                 substr.append(s[i].upper())
                
#             backTrack(i+1)
        
#         backTrack(0)
#         print(res)
                
            
            
            
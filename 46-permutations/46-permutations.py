class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []
        
        def dfs(curSet, remSet):
            
            if len(curSet)==len(nums):
                res.append(curSet.copy())
                return 
        
            
            for i in remSet:
                curSet.append(i)
                a = remSet.copy()
                a.remove(i)
                dfs(curSet, a)
                curSet.pop()
        
        dfs([], nums)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
        
        
#         def backtrack(subset, curSet):
#             if(len(subset)==len(nums)):
#                 res.append(subset.copy())
#                 return
            
#             for ele in curSet:
#                 subset.append(ele)
#                 a = curSet.copy()
#                 a.remove(ele)
#                 backtrack(subset, a)
#                 subset.pop()
                
                
#         backtrack([], nums)
#         return res




        
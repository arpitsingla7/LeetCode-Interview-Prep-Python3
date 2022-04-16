class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        candidates.sort()
        def dfs(curSum, i):
            if curSum==target:
                res.append(subset.copy())
                return 
            
            if i>=len(candidates) or curSum>target:
                return 
            
            subset.append(candidates[i])
            dfs(curSum+candidates[i], i+1)
            subset.pop()
            
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
        
            dfs(curSum, i+1)
        
        dfs(0, 0)
        return res
            
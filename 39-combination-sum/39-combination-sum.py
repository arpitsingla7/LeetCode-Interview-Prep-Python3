class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        curSet = []
        
        def dfs(i, curSum, curSet):
            if curSum==target:
                res.append(curSet.copy())
                return 
            if i>=len(candidates) or curSum>target:
                return 
            
            curSet.append(candidates[i])
            dfs(i, curSum+candidates[i], curSet)
            curSet.pop()
            
            dfs(i+1, curSum, curSet)
            
        
        dfs(0, 0, [])
        return res
                
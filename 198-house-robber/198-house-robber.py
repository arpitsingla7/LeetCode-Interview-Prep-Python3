class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return max(nums)
        
        elif len(nums)==3:
            return max(nums[0]+nums[2], nums[1])
        
        cache = {}
        
        def dfs(ind, curRes):
            if ind in cache:
                return cache[ind]
            
            if ind>=len(nums):
                return 
            
            curRes+=nums[ind]
            dfs(ind+2, curRes)
            cache[ind] = max(cache.get(ind+2, 0)+nums[ind], cache.get(ind+3, 0)+nums[ind], nums[ind])
            
            curRes-=nums[ind]
            dfs(ind+3, curRes)
            cache[ind] = max(cache.get(ind+2, 0)+nums[ind], cache.get(ind+3, 0)+nums[ind], nums[ind])
        
        dfs(0, 0)
        dfs(1, 0)
        return max(cache[0], cache[1])
            
        
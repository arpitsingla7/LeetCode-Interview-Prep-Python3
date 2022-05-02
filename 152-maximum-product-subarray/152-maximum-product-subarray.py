class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMin, curMax= 1, 1
        res = max(nums)
        
        for n in nums:
            if n==0:
                curMin, curMax = 1, 1
                continue
                
            tmp = curMax
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(n*tmp, n*curMin, n)
            
            res = max(res, curMax)
        return res
            
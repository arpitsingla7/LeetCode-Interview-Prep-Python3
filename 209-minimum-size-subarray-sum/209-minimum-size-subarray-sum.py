class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = len(nums)+1
        l, r = 0, 1
        tmp = nums[l]
        
        while l<r and r<=len(nums):
            while l<r and tmp>=target:
                res = min(res, r-l)
                tmp-=nums[l]
                l+=1
            
            if r<len(nums):
                tmp+=nums[r]
                r+=1
            else:
                r+=1
        
        return res if res!=len(nums)+1 else 0
            
                
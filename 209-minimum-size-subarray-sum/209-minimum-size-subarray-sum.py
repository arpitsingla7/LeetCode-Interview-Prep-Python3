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
            
            tmp += nums[r] if r<len(nums) else 0
            r+=1
        
        return res if res!=len(nums)+1 else 0
            
                
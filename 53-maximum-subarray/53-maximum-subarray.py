class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        tmp = nums[0]
        for i in (nums[1:]):
            if tmp<0:
                tmp = 0
                
            tmp+=i
            res = max(res, tmp)
        
        return res
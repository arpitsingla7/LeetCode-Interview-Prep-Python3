class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        temp = res = nums[0]
        
        for i in range(1, len(nums)):
            if temp<0:
                temp = 0
                
            temp += nums[i]
            res = max(res, temp)
        
        return res
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        temp = nums[0]
        for i in nums[1:]:
            
            if temp<0:
                temp = 0
            
            temp+=i
            res = max(res, temp)
        
        return res
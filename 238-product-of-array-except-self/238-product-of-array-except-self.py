class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        # [24, 12, 4, 1]
        # [24, 12, 8, 6]
        
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        suffix = 1
        for i in range(len(nums)-2, -1, -1):
            suffix = suffix*nums[i+1]
            prefix[i] = suffix*prefix[i]
        
        return prefix
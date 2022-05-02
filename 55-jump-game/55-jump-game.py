class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        res = [False]*len(nums)
        
        reach = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):                
            if (i+nums[i])>=reach:
                res[i] = True
                reach = i
        
        return res[0]
        
        
        
        
        
        
        
        
        
        
#         res = [False]*len(nums)
        
#         reach = len(nums)-1
        
#         for i in range(len(nums)-1, -1, -1):
#             for step in range(nums[i]+1):
                
#                 if (i+step)==reach and i+step<len(nums):
#                     res[i] = True
            
#             if res[i]:
#                 reach = i
        
#         return res[0]
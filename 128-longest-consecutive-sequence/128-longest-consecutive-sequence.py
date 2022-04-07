class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        res = 0
        
        for i in numSet:
            if i-1 not in numSet:
                tmp = 0
                while i+tmp in numSet:
                    tmp+=1
                
                res = max(res, tmp)
        return res
        
            
            
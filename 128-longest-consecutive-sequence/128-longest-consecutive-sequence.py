class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #starters:
        starters = []
        nums = set(nums)
        
        for i in nums:
            if i-1 not in nums:
                starters.append(i)
        res = 0
        for i in starters:
            temp = 1
            while i+1 in nums:
                temp+=1
                i+=1
            
            res = max(res, temp)
        
        return res
                
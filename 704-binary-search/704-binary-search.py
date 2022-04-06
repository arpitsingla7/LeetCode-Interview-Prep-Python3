class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        l, r = 0, len(nums)
        while l<r:
            m = l + (r-l)//2
            
            if nums[m]==target:
                return m
            
            if target>nums[m]:
                l = m+1
            
            else:
                r = m
        
        return -1
                
            
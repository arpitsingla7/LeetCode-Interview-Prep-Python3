class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        res = float("inf")
        while l<=r:
            if nums[l]<=nums[r]:
                res = min(res, nums[l])
            
            m = l + (r-l)//2
            res = min(res, nums[m])
            if nums[m]<=nums[r]:
                r = m-1
            else:
                l = m+1
        
        return res
            
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1
        while l<=r:
            i = l+ (r-l//2)
            if nums[i]==target:
                return i
            elif target<nums[i]:
                r = i-1
            else:
                l = i+1
        
        return -1
                
            
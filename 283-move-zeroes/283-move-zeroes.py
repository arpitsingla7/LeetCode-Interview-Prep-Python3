class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        numZero = 0
        length = len(nums)
        
        if 0 in nums:
            l = nums.index(0)
        else:
            return nums
        
        for r in range(l+1, length):
            if l!=r and nums[r]!=0:
                nums[l], nums[r] = nums[r], nums[l]
                while nums[l]!=0:
                    l+=1
        
        return nums
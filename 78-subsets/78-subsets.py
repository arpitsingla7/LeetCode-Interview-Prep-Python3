class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        def backTrack(i):
            
            if i>=len(nums):
                res.append(subset.copy())
                return 
            
            #includes the num[i]
            subset.append(nums[i])
            backTrack(i+1)
            
            
            #does not include that num[i]
            subset.pop()
            backTrack(i+1)
        
        backTrack(0)
        return res
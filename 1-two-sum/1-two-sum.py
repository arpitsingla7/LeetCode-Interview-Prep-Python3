class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #target-val: index(val)
        hashMap = {}
        
        for ind, val in enumerate(nums):
            if val in hashMap:
                return [hashMap[val], ind]
            
            hashMap[target-val] = ind
            
            
        
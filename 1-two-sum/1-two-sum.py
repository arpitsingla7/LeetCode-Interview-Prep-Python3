class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        hashMap = {}
        
        for i, val in enumerate(nums):
            if val in hashMap:
                return [i, hashMap[val]]
            
            hashMap[target-val] = i
        
        
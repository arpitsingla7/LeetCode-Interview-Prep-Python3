class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        l, r = 0, len(numbers)-1
        res = []
        
        while l<r:
            while numbers[l]+numbers[r]>target:
                r-=1
            
            while numbers[l]+numbers[r]<target:
                l+=1
            
            if numbers[l]+numbers[r] == target:
                return [l+1, r+1]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count the freq
        
        #make an arr of len of nums 
        #append to the index of arr as count and return from behind
        
        if len(nums)<=1:
            return nums
        
        countMap = {}
        for i in nums:
            countMap[i] = 1 + countMap.get(i, 0)
            
        resArr = [[] for i in range(len(nums)+1)]
        
        for i, val in countMap.items():
            resArr[val].append(i)
        
        print(resArr)
        res = []
        for i in range(len(resArr)-1, 0, -1):
            print(i)
            if len(res)!=k:
                res.extend(resArr[i])
            else:
                return res
        
        return res
            
            
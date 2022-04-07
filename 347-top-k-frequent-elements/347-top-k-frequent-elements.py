class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        #step 1: make a count dict
        countMap = {}
        for i in nums:
            countMap[i] = 1 + countMap.get(i, 0)
            
        print(countMap)
        #step 2: fill the countArr
        countArr = [[] for i in range(len(nums)+1)]
        for i, val in countMap.items():
            countArr[val].append(i)
        
        print(countArr)
        #step 3: find the first k 
        res = []
        for i in range(len(countArr)-1, 0, -1):
            res.extend(countArr[i])
            
            if len(res)==k:
                return res
        
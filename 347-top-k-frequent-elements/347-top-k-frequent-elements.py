class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        if len(nums)<=1:
            return nums
        
        countMap = {}
        for i in nums:
            countMap[i] = 1 + countMap.get(i, 0)
            
        resArr = []
        for i, val in countMap.items():
            resArr.append((-1*val, i))
        heapq.heapify(resArr)
        
        res = []
        while len(res)!=k:
            res.append(heapq.heappop(resArr)[1])
            
        return res
            
            
            
        
#         resArr = [[] for i in range(len(nums)+1)]
        
#         for i, val in countMap.items():
#             resArr[val].append(i)
        
#         res = []
#         for i in range(len(resArr)-1, 0, -1):
#             if len(res)!=k:
#                 res.extend(resArr[i])
#             else:
#                 return res
        
#         return res
            
            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        count = {}
        
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            
        
        res = []
        freq = [[] for i in range(len(nums)+1)]
        
        for i, val in count.items():
            freq[val].append(i)
            
        
        for i in range(len(freq)-1, 0, -1):
            if len(freq[i])!=0:
                res.extend(freq[i])
                
                if len(res)==k:
                    return res
        
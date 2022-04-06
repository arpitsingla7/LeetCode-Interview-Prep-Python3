class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        count = {}
        
        for i in nums:
            if i in count:
                count[i]+=1
                continue
            count[i] = 1
            
        
        res = []
        freq = [[] for i in range(len(nums)+1)]
        
        for i, val in count.items():
            freq[val].append(i)
            
        print(freq)
        for i in range(len(freq)-1, 0, -1):
            if len(freq[i])!=0:
                
                res.extend(freq[i])

                if len(res)==k:
                    return res
        
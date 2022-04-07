class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-1*i for i in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            s1 = -1*heapq.heappop(stones)
            s2 = -1*heapq.heappop(stones)
            
            if s1!=s2:
                diff = abs(s1-s2)
                heapq.heappush(stones, diff*-1)
    
        
        if stones: return -1*stones[0] 
        else: return 0
            
                
                
            
                
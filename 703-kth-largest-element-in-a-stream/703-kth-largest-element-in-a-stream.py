class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.numsHeap = nums
        heapq.heapify(self.numsHeap)
        
        while len(self.numsHeap)>k:
            heapq.heappop(self.numsHeap)
            

    def add(self, val: int) -> int:
        if len(self.numsHeap)<self.k:
            heapq.heappush(self.numsHeap, val)
        
        else:
            if val>self.numsHeap[0]:
                heapq.heappush(self.numsHeap, val)
                heapq.heappop(self.numsHeap)
        
        return self.numsHeap[0]
            
        
         
        
        
        
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
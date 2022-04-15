class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [i*(-1) for i in nums]        
        heapq.heapify(nums)
        
        
        for i in range(k):
            res = heapq.heappop(nums)
        
        return (-1)*res
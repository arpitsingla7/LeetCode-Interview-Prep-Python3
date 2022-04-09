class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r
        
        while l<=r:
            k = l + (r-l)//2
            tmp = 0
            for i in piles:
                tmp+= ceil(i/k)
            
            if tmp<=h:
                r = k-1
                res = min(res, k)
            else:
                l = k+1
        return res
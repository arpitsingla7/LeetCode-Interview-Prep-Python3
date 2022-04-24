class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        l, r = 1, max(piles)
        res = r
        
        while l<=r:
            m = l + (r-l)//2
            tmp = 0
            #how to calculate no. of hours 
            for i in piles:
                tmp+=ceil(i/m)
            
            #how to decide the rate
            if tmp<=h:
                r = m-1
                res = min(res, m)
            else:
                l=m+1
        
        return res
                
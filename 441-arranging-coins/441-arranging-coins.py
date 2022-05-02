class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        
        l, r = 0, n
        res = 0
        while l<=r:
            m = (l+r)//2
            s = math.ceil((m/2)*(m+1))
            
            if s>n:
                r = m-1
            elif s<n:
                l = m+1
                if m>res:
                    res = m
            else:
                return m
            
        return res
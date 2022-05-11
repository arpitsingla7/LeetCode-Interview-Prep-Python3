class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a, b, c = target[0], target[1], target[2]
        p = 0
        check = [0, 0, 0]
        for ind, t in enumerate(triplets):
            x, y, z = t[0], t[1], t[2]
            if (x<=a and y<=b and z<=c):
                p+=1
            
                if x==a:
                    check[0] = 1
                
                if y==b:
                    check[1] = 1
                
                if z==c:
                    check[2] = 1
        
            if sum(check)==3:
                return True
            
        if sum(check)!=3 or p==0:
            return False
        
        # return True
        
    
                
            
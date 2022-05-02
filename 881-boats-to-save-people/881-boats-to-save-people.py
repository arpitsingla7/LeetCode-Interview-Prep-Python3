class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
    
        
        
        people = sorted(people) 
        res = 0
        l, r = 0, len(people)-1
        
        while l<=r:
            if l==r:
                res+=1
                break
                
            total = people[l]+people[r]
            
            if total>limit:
                r-=1
                res+=1
            else:
                l+=1
                r-=1
                res+=1
        
        return res
                
                
        
        
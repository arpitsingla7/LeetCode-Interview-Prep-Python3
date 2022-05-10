class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        start = [(i[1], i[0]) for i in trips]
        start.sort(key = lambda i: i[0])
        
        end = [(i[2], i[0]) for i in trips]
        end.sort(key = lambda i: i[0])
        
        s, e = 0, 0
        res, count = 0, 0
        
        while s<len(start):
            if start[s][0]<end[e][0]:
                count+=start[s][1]
                s+=1
            else:
                count-=end[e][1]
                e+=1
            
            # res = max(res, count)
            if count>capacity:
                return False
        
        return True if res<=capacity else False
                
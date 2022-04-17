class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda i: i[0])
        res = []
        for i in range(len(intervals)-1):
            if intervals[i][1]<intervals[i+1][0]:
                res.append(intervals[i])
                pass
            else:
                intervals[i+1] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                
        return res+[intervals[-1]]
            
        
        
        
        
        
        
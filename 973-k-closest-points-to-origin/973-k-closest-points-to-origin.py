class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        """
        
            initializ a heap of this [(dist, (x, y))]

        """
        
        #dist = (i[0]**2 + i[1]**2)**(0.5)
        points = [((i[0]**2 + i[1]**2)**(0.5), i) for i in points]
        
        heapq.heapify(points)
        res = []
        
        while len(res)!=k:
            point = heapq.heappop(points)
            res.append(point[1])
        
        return res
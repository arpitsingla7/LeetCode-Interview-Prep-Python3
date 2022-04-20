class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        a, b = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            
            temp = cost[i] + min(a, b)
            
            a, b = b, temp
        
        return min(a, b)
        
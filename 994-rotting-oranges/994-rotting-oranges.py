class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #initialize a queue with rotten tomatoes
        #find all the rotten tomatoes
        rows, cols = len(grid), len(grid[0])
        totalNotRot = 0
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c,0))
                elif grid[r][c]==1:
                    totalNotRot+=1
        
        def dfs(r, c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or grid[r][c]==2):
                return False
            else:
                return True
        
        res = 0
        while q:
            
            r, c, tmp = q.popleft()
            res = max(res, tmp)
            if dfs(r+1, c):
                grid[r+1][c]=2
                q.append((r+1, c, tmp+1))
                totalNotRot-=1
                
            if dfs(r-1, c):
                grid[r-1][c]=2
                q.append((r-1, c, tmp+1))
                totalNotRot-=1
                
            if dfs(r, c+1):
                grid[r][c+1]=2
                q.append((r, c+1, tmp+1))
                totalNotRot-=1

            if dfs(r, c-1):
                grid[r][c-1]=2
                q.append((r, c-1, tmp+1))
                totalNotRot-=1
        
        if totalNotRot!=0: return -1
        return res
    
    
    
#     class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
        
#         #initialize a queue with rotten tomatoes
#         #find all the rotten tomatoes
#         rows, cols = len(grid), len(grid[0])
#         totalNotRot = 0
#         q = deque()
        
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]==2:
#                     q.append((r,c,0))
#                 elif grid[r][c]==1:
#                     totalNotRot+=1
        
#         def dfs(r, c):
#             if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or grid[r][c]==2):
#                 return False
#             else:
#                 return True
        
#         res = 0
#         explore = [("r+1", "c"), ("r-1", "c"), (r, c+1), (r, c-1)]
#         while q:
            
#             r, c, tmp = q.popleft()
#             res = max(res, tmp)
            
#             for e in explore:
#                 R, C = e[0], e[1]
#                 print(e[0])
#                 if dfs(R, C):
#                     grid[R][C]=2
#                     q.append((R, C, tmp+1))
#                     totalNotRot-=1
            
# #             if dfs(r+1, c):
# #                 grid[r+1][c]=2
# #                 q.append((r+1, c, tmp+1))
# #                 totalNotRot-=1
                
# #             if dfs(r-1, c):
# #                 grid[r-1][c]=2
# #                 q.append((r-1, c, tmp+1))
# #                 totalNotRot-=1
                
# #             if dfs(r, c+1):
# #                 grid[r][c+1]=2
# #                 q.append((r, c+1, tmp+1))
# #                 totalNotRot-=1

# #             if dfs(r, c-1):
# #                 grid[r][c-1]=2
# #                 q.append((r, c-1, tmp+1))
# #                 totalNotRot-=1
        
#         if totalNotRot!=0: return -1
#         return res
                
        
        
        
        
                
        
        
        
        
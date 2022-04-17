class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        ROWS, COLS = len(board), len(board[0])
        path = set()
        self.res = False
        
        def dfs(r, c, ind):
            
            if len(word)==ind:
                self.res = True
                return
            
            if (r<0 or c<0 or r>=ROWS or c>=COLS or 
                board[r][c]!=word[ind] or (r, c) in path):
                return
            
            path.add((r, c))
            
            dfs(r+1, c, ind+1) 
            dfs(r-1, c, ind+1)
            dfs(r, c+1, ind+1)
            dfs(r, c-1, ind+1)
            path.remove((r, c))
    
    
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in path:
                    dfs(i, j, 0)
                    if self.res:
                        return self.res
        
        return False
            
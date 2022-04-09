class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, m):
            if(target <= matrix[i][n-1]):
                for j in range(0, n):
                    if(target == matrix[i][j]):
                        return True
                    else:
                        pass
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        top, bot = 0, len(matrix)-1
        while top<=bot:
            row = (top+bot)//2
            
            if target<matrix[row][0]:
                bot = row-1
            elif target>matrix[row][-1]:
                top = row+1
            else:
                break
            
        
        if not (top<=bot):
            return False
        
        l, r = 0, len(matrix[row])-1
        row = matrix[row]
        while l<=r:
            m = l+(r-l)//2

            if target==row[m]:
                return True
            elif target<row[m]:
                r=m-1
            else:
                l=m+1
        return False
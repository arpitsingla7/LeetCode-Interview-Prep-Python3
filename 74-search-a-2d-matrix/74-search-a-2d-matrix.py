class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        for row in matrix:
            if row[0]<=target<=row[-1]:
                l, r = 0, len(row)-1
                while l<=r:
                    m = l+(r-l)//2
                    
                    if target==row[m]:
                        return True
                    elif target<row[m]:
                        r=m-1
                    else:
                        l=m+1
        return False
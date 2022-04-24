class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #find the row
        for r in matrix:
            if target<=r[-1]:
                break
        
        #find the target
        row = r
        l, r = 0, len(row)-1
        while l<=r:
            m = l + (r-l)//2
            
            if row[m]==target:
                return True
            elif target<row[m]:
                r=m-1
            else:
                l=m+1
        
        return False
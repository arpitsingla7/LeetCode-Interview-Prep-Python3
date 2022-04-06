class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l, r = 0, len(matrix)-1
        
        while l<r:
            
            for i in range(r-l):
                
                t, b = l, r
                
                #store the top left val
                topLeft = matrix[t][l+i]
                
                #move bottom left to top left:
                matrix[t][l+i] = matrix[b-i][l]
                
                #move bottom right to bottom left:
                matrix[b-i][l] = matrix[b][r-i]
                
                #move top right to bottom right:
                matrix[b][r-i] = matrix[t+i][r]
                
                #move top left to top right:
                matrix[t+i][r] = topLeft
                
            l+=1
            r-=1
                
            
                
            
            
            
            
            
            
            
                
            
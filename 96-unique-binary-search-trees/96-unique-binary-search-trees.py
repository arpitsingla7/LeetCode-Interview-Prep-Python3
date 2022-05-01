class Solution:
    def numTrees(self, n: int) -> int:
        
        res = [1] * (n+1)
        
        for i in range(2, n+1):
            tmp = 0
            for root in range(1, i+1):
                right = i - root
                left = i - (right+1)
                tmp+=res[left]*res[right]
            res[i] = tmp
        
        return res[n]
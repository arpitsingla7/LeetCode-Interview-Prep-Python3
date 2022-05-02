class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #method 1 o(m+n)
        
        numIndx = {n:i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)
        
        stack = []
        for i in nums2:
            
            cur = i
            while stack and cur>stack[-1]:
                val = stack.pop()
                indx = numIndx[val]
                res[indx] = cur
            
            if cur in numIndx:
                stack.append(cur)
        
        return res
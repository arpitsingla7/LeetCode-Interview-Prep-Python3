# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        #bfs method
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
            
        queue = [[p, q]]
        
        while queue:
            
            p, q = queue.pop(0)
            
            if p and q:
                if p.val != q.val:
                    return False
                queue.append([p.left, q.left])
                queue.append([p.right, q.right])
            
            elif p or q:
                return False
                    
        return True
            
            
            
            
            
            
            
            
            
            
            
            
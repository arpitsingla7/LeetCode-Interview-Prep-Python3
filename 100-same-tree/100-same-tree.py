# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        #recursive method:
        
        def dfs(p, q):
            if not p and not q:
                return True
            
            if (not p and q) or (p and not q):
                return False
            
            balance = (p.val == q.val) and dfs(p.left, q.left) and dfs(p.right, q.right)
            
            return balance
        
        return dfs(p, q)
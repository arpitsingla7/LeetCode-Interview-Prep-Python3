# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def dfs(pNode, qNode):
            if not pNode and not qNode:
                return True
            if (not pNode and qNode) or (pNode and not qNode):
                return False
            
            balance = ((pNode.val==qNode.val) and dfs(pNode.left, qNode.left) and 
                       dfs(pNode.right, qNode.right))
            
            return balance
        
        return dfs(p, q)
            
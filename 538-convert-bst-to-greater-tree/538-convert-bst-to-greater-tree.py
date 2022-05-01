# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        cur = 0
        def dfs(root):
            if not root:
                return 
            
            nonlocal cur
            dfs(root.right)
            
            temp = root.val
            root.val += cur
            cur += temp
            
            dfs(root.left)
        
        dfs(root)
        return root
            
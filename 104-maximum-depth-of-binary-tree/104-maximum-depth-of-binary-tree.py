# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #dfs
        def dfs(root, level):
            if not root:
                return 0
            
            level = 1+ max(dfs(root.left, level), dfs(root.right, level))
            
            return level
            
        
        
        return dfs(root, 0)
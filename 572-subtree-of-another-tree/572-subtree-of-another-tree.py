# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        hashMap = {}
        self.res = False
        
        def dfs(node, path):
            
            if not node or self.res:
                return "N"
            
            path = str(node.val) + dfs(node.left, path) + dfs(node.right, path)
            
            if path in hashMap:
                self.res = True
            
            return path
        
        
        hashMap[dfs(subRoot, "")] = 1
        dfs(root, "")
        
        return self.res
        
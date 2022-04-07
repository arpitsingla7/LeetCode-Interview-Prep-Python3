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
        def dfs(root, path):
            if not root:
                return "#"
            
            path += str(root.val) + "-" + dfs(root.left, path) + "-" + dfs(root.right, path)
            
            if path in hashMap:
                self.res = True
            
            return path
        
        subPath = dfs(subRoot, "")
        hashMap[subPath] = 1
        dfs(root, "")
        return self.res
            
            
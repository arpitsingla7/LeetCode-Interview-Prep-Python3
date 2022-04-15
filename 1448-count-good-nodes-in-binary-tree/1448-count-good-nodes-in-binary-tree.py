# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0
        def dfs(root, path, m):
            if not root:
                return ""
            
            # path += str(root.val) + ","
            m = max(m, root.val)
            if m<=root.val:
                self.res+=1
            # print(m, m<=root.val)
            # path.append(root.val)

            dfs(root.left, path, m)
            
            dfs(root.right, path, m)
            
            
            return path
        
        dfs(root, "", root.val)
        return self.res
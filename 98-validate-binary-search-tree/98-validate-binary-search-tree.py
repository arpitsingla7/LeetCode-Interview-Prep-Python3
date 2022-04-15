# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True
        def dfs(root, MIN, MAX):
            if not root:
                return 
            
            if root.val>MIN and root.val<MAX:
                dfs(root.left, MIN, root.val)
                dfs(root.right, root.val, MAX)
                    
            else:
                self.res = False
            
        
        
        MIN = float("-inf")
        MAX = float("inf")
        dfs(root, MIN, MAX)
        return self.res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        self.res = True
        
        def dfs(root, curMin, curMax):
            if not root or not self.res:
                return 
            
            if root.val>curMin and root.val<curMax:
                dfs(root.left, curMin, root.val)
                dfs(root.right, root.val, curMax)
            else:
                self.res = False        
        
        
        curMin, curMax = float("-inf"), float("inf")
        dfs(root, curMin, curMax)
        return self.res
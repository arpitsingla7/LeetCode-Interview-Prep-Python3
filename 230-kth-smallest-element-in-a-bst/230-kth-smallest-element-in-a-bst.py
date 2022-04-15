# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 0
        self.res = 0
        def dfs(root):
            if not root or self.count==k:
                return 
            
            print(root.val)
            dfs(root.left)
            
            self.count+=1
            if k==self.count:
                self.res = root.val
                return
            
            dfs(root.right)
        
        dfs(root)
        return self.res
        
        
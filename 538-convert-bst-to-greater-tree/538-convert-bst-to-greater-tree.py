# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 1, 2, 3, 5, 7, 10
        #27,25,22,17,10, 10
        self.total = 0
        def dfs(root):
            if not root:
                return 
            
            self.total+=root.val
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        def greaterTree(root):
            if not root:
                return 
        
            greaterTree(root.left)
            
            temp = root.val
            root.val = self.total
            self.total -= temp
            
            greaterTree(root.right)
        
        greaterTree(root)
        return root
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        def dfs(pre, ind):
            if not pre or not ind:
                return
            
            
            root = TreeNode(pre[0])
            m = ind.index(pre[0])
            
            root.left = dfs(pre[1:m+1], ind[:m])
            
            root.right = dfs(pre[m+1:], ind[m+1:])
            
            return root
        
        return dfs(preorder, inorder)
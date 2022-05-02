# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(pre, inord):
            if not pre or not inord:
                return 
            
            node = TreeNode(pre[0])
            idx = inord.index(pre[0])
            
            node.left = dfs(pre[1: idx+1], inord[:idx])
            node.right = dfs(pre[idx+1:], inord[idx+1:])
            
            return node
    
        return dfs(preorder, inorder)
        
        
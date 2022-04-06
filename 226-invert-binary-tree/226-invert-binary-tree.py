# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return 
        
        queue = deque([root])
        while queue:
            
            node = queue.pop()
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return root
        
 










        
        
        
        
        
        
        
        
#         #**********bfs**********
#         if not root:
#             return root
        
#         q = deque([root])
        
#         while q:
#             node = q.popleft()
#             node.left, node.right = node.right, node.left
            
#             if node.left:
#                 q.append(node.left)
            
#             if node.right:
#                 q.append(node.right)
        
#         return root
        
        
#         #**********recursive dfs*************
#         def dfs(root):
            
#             if not root:
#                 return root
            
#             root.left, root.right = root.right, root.left
#             dfs(root.left)
#             dfs(root.right)
            
#             return root
    
#         #return dfs(root)
            
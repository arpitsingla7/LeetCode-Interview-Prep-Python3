# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if length==1:
                    res.append(node.val)
                length-=1
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            
        return res
                
                
                
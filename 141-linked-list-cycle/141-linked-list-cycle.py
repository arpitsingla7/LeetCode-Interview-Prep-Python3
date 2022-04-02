# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        nodeSet = set()
        node = head
        while node:
            if node in nodeSet:
                return True
            nodeSet.add(node)
            node = node.next
        
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #recursive method:
        if not head: return 
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead
        
        #iterative method
        prev = None
        node = head
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        
        return prev
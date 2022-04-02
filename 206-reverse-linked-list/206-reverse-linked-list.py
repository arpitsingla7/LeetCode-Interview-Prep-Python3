# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #recursive method
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
            
        return newHead
        
        
        
        
        #iterative method
#         prev = None
#         cur = head
#         while cur: 
#             temp = cur.next
#             cur.next = prev
#             prev = cur
#             cur = temp
           
#         return prev
           
        
        
            
            
        
        
        
                
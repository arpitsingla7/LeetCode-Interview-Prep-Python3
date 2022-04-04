# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return 
        
        length = 0
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            length+=2
        
        if fast:
            length+=1        
        
        if length==1:
            return None
        
        prev.next = prev.next.next
        return head
        
        
        
        
        
        
        
        
        
        
        
        
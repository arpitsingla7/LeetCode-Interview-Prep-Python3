# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev
        first = head
        slow.next = None
        
        
        while second:
            node1 = first.next
            node2 = second.next
            
            first.next = second
            second.next = node1
            first = node1
            second = node2
        
        return head
        
        
        
        
        
        
        
        
        
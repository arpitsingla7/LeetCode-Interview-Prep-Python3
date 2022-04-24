# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return 
        
        length = 0
        node = head
        while node:
            length+=1
            node = node.next
        
        if n==length:
            return head.next
            
        
        node = head
        travel = 1
        while travel!=(length-n):
            node = node.next
            travel+=1
        
        node.next = node.next.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        #find the length of the list
        length = 0
        node = head
        while node:
            length+=1
            node = node.next
        
        if n==length:
            return head.next
        
        #stop at the prev node 
        node = head
        for i in range(length-(n+1)):
            node = node.next
        
        #switch the pointers
        node.next = node.next.next
        
        return head
        
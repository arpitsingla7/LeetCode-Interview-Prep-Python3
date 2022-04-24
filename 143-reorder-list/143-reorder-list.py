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
        
        if not head: return 
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse the list
        list2 = slow.next
        prev, slow.next = None, None
        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt
        
        list2 = prev
        list1 = head
        
        while list2:
            nxt1, nxt2 = list1.next, list2.next
            list1.next, list2.next = list2, nxt1
            list1, list2 = nxt1, nxt2
        
        
            
            
            
            
            
            
        
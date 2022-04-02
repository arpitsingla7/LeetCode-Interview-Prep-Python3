# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
       
        if len(lists)==0:
            return None
        
        if len(lists)==1:
            return lists[0]
        
        while len(lists)!=1:
            dummy = ListNode()
            tail = dummy
            list1 = lists[0]
            list2 = lists[1]
            
            while list1 and list2:
                if list1.val<list2.val:
                    tail.next = list1
                    list1 = list1.next
                
                else:
                    tail.next = list2
                    list2 = list2.next
                    
                tail = tail.next
            
            if list1:
                tail.next = list1
            elif list2:
                tail.next = list2
            
            lists.pop(0)
            lists.pop(0)
            lists.insert(0, dummy.next)
            
        return lists[0]
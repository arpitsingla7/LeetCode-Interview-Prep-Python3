"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hashMap = {}
        
        def createList(node, orgNode):
            
            #base case:
            if not orgNode:
                node.next = None
                hashMap[orgNode] = node.next
                return 
            
            node.next = Node(orgNode.val)
            hashMap[orgNode] = node.next
            createList(node.next, orgNode.next)
            
                
        dummy = Node(0)
        tail = dummy
        createList(tail, head)
        
        node = tail.next
        orgNode = head
        while node:
            ran = hashMap[orgNode.random]
            node.random = ran
            node = node.next
            orgNode = orgNode.next
        
        return tail.next
        
        
            
            
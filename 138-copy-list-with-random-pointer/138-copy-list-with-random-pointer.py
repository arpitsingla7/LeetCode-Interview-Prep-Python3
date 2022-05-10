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
        
        if not head: return None
        
        #map to show mappin from node to newNode
        nodeMap = {} #old to new
        node = head
        while node:
            nodeMap[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            newNode = nodeMap[node]
            
            newNode.next = nodeMap[node.next] if node.next else None
            newNode.random = nodeMap[node.random] if node.random else None
            
            node = node.next
        
        return nodeMap[head]
            
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left

        
    def addNode(self, node):
        #add node to linked list
        #add to the right always 
        prev, nxt = self.right.prev, self.right
        node.prev, node.nxt = prev, nxt
        prev.nxt, nxt.prev = node, node
    
    def removeNode(self, node):
        #remove node from linked list
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.addNode(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        
        self.cache[key] = ListNode(key, value)
        self.addNode(self.cache[key])
        
        if len(self.cache)>self.capacity:
            lru = self.left.nxt
            self.removeNode(self.cache[lru.key])
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
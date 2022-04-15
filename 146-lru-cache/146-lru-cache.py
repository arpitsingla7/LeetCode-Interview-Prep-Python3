class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        
        self.left.nxt = self.right
        self.right.prev = self.left
        

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        nxt.prev, prev.nxt = prev, nxt
    
    def add(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.nxt = prev, nxt
        prev.nxt = nxt.prev = node
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            #update the most recently used key in cache
            #remove from where the node is 
            self.remove(self.cache[key])
            #add the node to righmost point
            self.add(self.cache[key])
            
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #do we need to update the cache 
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        
        
        if self.capacity<len(self.cache):
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
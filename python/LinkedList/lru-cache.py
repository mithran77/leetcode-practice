class dllNode:

    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Maps keys to DLL Nodes
        self.left, self.right = dllNode(0, 0), dllNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        # Remove links
        prev.next, next.prev = next, prev

    # Inserts at right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        # Insert Node
        prev.next = next.prev = node
        # New node's pointers
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Insert
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = dllNode(key, value)
        self.insert(self.cache[key])
        # Capacity check
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del(self.cache[lru.key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

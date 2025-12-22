# 146. LRU Cache

# Design a data structure that follows the constraints of a Least Recently
# Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1. void put(int key, int value) Update the value of the key if the
# key exists. Otherwise, add the key-value pair to the cache. If the number of
# keys exceeds the capacity from this operation, evict the least recently used
# key. The functions get and put must each run in O(1) average time complexity.

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# class dllNode:

#     def __init__(self, key, val) -> None:
#         self.key, self.val = key, val
#         self.next = self.prev = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {} # { key: dllNode }
#         self.left, self.right = dllNode(0, 0), dllNode(0, 0)
#         self.left.next, self.right.prev = self.right, self.left
#         # left <> LRU ... MRU <> right

#     # Unlinks node from LinkedList
#     def remove(self, node):
#         p, n = node.prev, node.next
#         # Remove links
#         p.next, n.prev = n, p

#     # Inserts new node as MRU
#     def insert(self, node):
#         p, n = self.right.prev, self.right
#         # Insert Node
#         p.next = n.prev = node
#         # New node's pointers
#         node.prev, node.next = p, n

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             # Insert value as MRU
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             # Return MRU.val
#             return self.cache[key].val
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         # Always overwrite
#         self.cache[key] = dllNode(key, value)
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.insert(self.cache[key])
#         # Capacity check
#         if len(self.cache) > self.capacity:
#             lru = self.left.next
#             self.remove(lru)
#             del(self.cache[lru.key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = DLLNode(0, 0), DLLNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # Removes last existing reference
            self.remove(self.cache[key])
        self.cache[key] = DLLNode(key, value)
        self.insert(self.cache[key])
        # Take care of capacity
        if len(self.cache) > self.capacity:
            while len(self.cache) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del (self.cache[key])

    def remove(self, node: DLLNode):  # Unlink from DLL
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def insert(self, node: DLLNode):  # Insert as MRU
        p, n = self.right.prev, self.right
        p.next = n.prev = node
        node.prev, node.next = p, n

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

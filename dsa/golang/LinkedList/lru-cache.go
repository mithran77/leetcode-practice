/*
    https://leetcode.com/problems/lru-cache
    146. LRU Cache

    Design a data structure that follows the constraints of a Least Recently
    Used (LRU) cache.

    Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise
    return -1. void put(int key, int value) Update the value of the key if the
    key exists. Otherwise, add the key-value pair to the cache. If the number of
    keys exceeds the capacity from this operation, evict the least recently used
    key. The functions get and put must each run in O(1) average time complexity.

    Example 1:

    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4

    Constraints:

    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.

*/

type DLLNode struct {
    Val int
    Key int
    Prev *DLLNode
    Next *DLLNode
}

type LRUCache struct {
    cache map[int]*DLLNode
    capacity int
    left *DLLNode
    right *DLLNode
}


func Constructor(capacity int) LRUCache {
    l := LRUCache{
        cache: map[int]*DLLNode{},
        capacity: capacity,
        left: &DLLNode{},
        right: &DLLNode{},
    }
    l.left.Next = l.right
    l.right.Prev = l.left
    return l
}


func (l *LRUCache) Get(key int) int {
    if n, exists  := l.cache[key]; exists {
        l.Remove(n)
        l.Insert(n)
        return n.Val
    }
    return -1
}


func (l *LRUCache) Put(key int, value int)  {
    // Insert
    if n, exists  := l.cache[key]; exists {
        l.Remove(n)
        delete(l.cache, key)
    }
    n := &DLLNode{Key: key, Val: value}
    l.Insert(n)
    l.cache[key] = n

    // Capacity check
    for len(l.cache) > l.capacity {
        lru := l.left.Next
        delete(l.cache, lru.Key)
        l.Remove(lru)
    }
}

func (l *LRUCache) Remove(node *DLLNode)  {
    p, n := node.Prev, node.Next
    p.Next, n.Prev = n, p
}

func (l *LRUCache) Insert(node *DLLNode)  {
    p := l.right.Prev
    p.Next = node
    node.Next, node.Prev = l.right, p
    l.right.Prev = node
}



/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
# 138. Copy List with Random Pointer

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
# where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the
# original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two
# nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Constraints:

# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# # Recursive
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         node_map = {}

#         if not head:
#             return None

#         def dfs(node):
#             # BC
#             if node in node_map:
#                 return node_map[node]
#             node_map[node] = Node(node.val)
#             # RC
#             if node.next:
#                 node_map[node].next = dfs(node.next)
#             if node.random:
#                 node_map[node].random = dfs(node.random)
#             return node_map[node]

#         dfs(head)
#         return node_map[head]

# Iterative
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}

        if not head:
            return None

        def dfs(node):
            # BC
            if node in node_map:
                return node_map[node]
            node_map[node] = Node(node.val)
            # RC
            if node.random:
                node_map[node].random = dfs(node.random)
            if node.next:
                node_map[node].next = dfs(node.next)
            return node_map[node]

        dfs(head)
        return node_map[head]

# # Iterative one pass
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         node_map = {}

#         if not head:
#             return None

#         # Next
#         cur = head
#         while cur:

#             node_map[cur] = Node(cur.val)
#             if cur.next:
#                 node_map[cur].next = Node(cur.next.val)
#             else:
#                 node_map[cur].next = None

#             if cur.random:
#                 if cur.random in node_map:
#                     node_map[cur].random = node_map[cur.random]
#                 else:
#                     node_map[cur].random = Node(cur.random.val)
#             else:
#                 node_map[cur].random = None

#             cur = cur.next

#         return node_map[head]


if __name__ == '__main__':
    res = Solution()
    print(res.copyRandomList(head = [[7, None],[13, 0],[11, 4],[10, 2],[1, 0]]))
    print(res.copyRandomList(head = [[1, 1],[2, 1]]))
    print(res.copyRandomList(head = [[3, None],[3, 0],[3, None]]))


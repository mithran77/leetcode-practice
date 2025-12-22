# 100. Same Tree

# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not. Two binary trees are considered the same if they
# are structurally identical, and the nodes have the same value.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:

# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

from typing import Optional
import importlib
bt = importlib.import_module("lc-binary-tree")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#    def isSameTree(
#        self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # Base cases

#         # if Both None: True
#         if not p and not q:
#             return True

#         # if Either None or Value mismatch: False
#         if not p or not q or (p.val != q.val):
#             return False

#         # Recursive case
#         # if l==r: True; else: False
#         return (
#             self.isSameTree(p.left, q.left)
#             and self.isSameTree(p.right, q.right)
#         )


# class Solution:
#    def isSameTree(
#        self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

#         def rSameTree(n1: TreeNode, n2: TreeNode) -> bool:
#             # DFS Preorder

#             # BCs
#             if not n1 and not n2:
#                 return True

#             # RCs
#             if not n1 or not n2:
#                 return False
#             if n1.val != n2.val:
#                 return False

#             return (  # AND will short circuit if False
#                 rSameTree(n1.left, n2.left) and
#                 rSameTree(n1.right, n2.right)
#             )

#         return rSameTree(p, q)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def rSameTree(n1: TreeNode, n2: TreeNode) -> bool:
            # DFS Preorder

            # BCs
            if not n1 and not n2:
                return True

            # RCs
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False

            if not rSameTree(n1.left, n2.left):
                return False
            if not rSameTree(n1.right, n2.right):
                return False

            return True

        return rSameTree(p, q)


if __name__ == "__main__":
    p = bt.build_tree([1, 2, 3])
    q = bt.build_tree([1, 2, 3])
    print(Solution().isSameTree(p, q))
    p = bt.build_tree([1, 2])
    q = bt.build_tree([1, None, 2])
    print(Solution().isSameTree(p, q))
    p = bt.build_tree([1, 2, 1])
    q = bt.build_tree([1, 1, 2])
    print(Solution().isSameTree(p, q))

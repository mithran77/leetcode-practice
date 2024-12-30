# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from typing import Optional, List
import importlib
bt = importlib.import_module("lc-binary-tree")
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # Iterative
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         if not root:
#             return res

#         q = deque([root])
#         while q:
#             right_side = None
#             q_len = len(q)
#             for _ in range(q_len):
#                 e = q.popleft()
#                 right_side = e.val # Overwrite level
#                 if e.left:
#                     q.append(e.left)
#                 if e.right:
#                     q.append(e.right)

#             if right_side is not None:
#                 res.append(right_side)

#         return res

# Recursive
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def recurseLevels(node, level):
            if not node:
                return
            if len(res) > level:
                res[level] = node.val # Overwrite
            else:
                res.append(node.val)
            recurseLevels(node.left, level + 1)
            recurseLevels(node.right, level + 1)

        recurseLevels(root, 0)
        return res


if __name__ == "__main__":
    root = bt.build_tree([1,2,3,None,5,None,4])
    print(Solution().rightSideView(root))
    root = bt.build_tree([1,None,3])
    print(Solution().rightSideView(root))
    root = bt.build_tree([0,1,2,None,3,4,None,None,5,9,None,None,6,10,None])
    print(Solution().rightSideView(root))

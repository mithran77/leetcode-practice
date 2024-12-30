from typing import List, Optional
from collections import deque
import importlib
bt = importlib.import_module("lc-binary-tree")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def recurseLevels(node, level):
            if not node:
                return
            if len(res) < level:
                res.append([])
            res[level].append(node.val)

            recurseLevels(node.left, level + 1)
            recurseLevels(node.right, level + 1)

        recurseLevels(root, 0)
        return res

# # Iterative
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
#         q = deque()
#         q.append(root)

#         while q:
#             level = []
#             q_len = len(q)
#             for i in range(q_len):
#                 node = q.popleft()
#                 if node is not None:
#                     level.append(node.val)
#                     q.append(node.left)
#                     q.append(node.right)
#             if level != []:
#                 res.append(level)

#         return res

if __name__ == "__main__":
    root = bt.build_tree([3, 9, 20, None, None, 15, 7])
    print(Solution().levelOrder(root))
    root = bt.build_tree([1])
    print(Solution().levelOrder(root))
    root = bt.build_tree([])
    print(Solution().levelOrder(root))

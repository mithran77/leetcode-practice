# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true


# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
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
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         self.balanced = True

#         def maxHeight(node: TreeNode | None):
#             if node is None:
#                 return 0

#             lh = maxHeight(node.left)
#             rh = maxHeight(node.right)
#             if self.balanced and abs(lh-rh) > 1:
#                 self.balanced = False

#             return 1 + max(lh, rh), abs(lh-rh) <= 1

#         maxHeight(root)

#         return self.balanced

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def maxHeight(n):
            if not n:
                return 0

            lh = maxHeight(n.left)
            if lh == -1: return -1
            rh = maxHeight(n.right)
            if rh == -1: return -1

            if abs(lh -rh) > 1:
                 return -1

            return 1 + max(lh, rh)

        if maxHeight(root) != -1:
            return True
        else:
            return False

if __name__ == "__main__":
    root = bt.build_tree([3,9,20,None,None,15,7])
    print(Solution().isBalanced(root))
    root = bt.build_tree([1,2,2,3,3,None,None,4,4])
    print(Solution().isBalanced(root))
    root = bt.build_tree([])
    print(Solution().isBalanced(root))
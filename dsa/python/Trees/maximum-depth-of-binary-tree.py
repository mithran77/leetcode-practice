# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes
# along the longest path from the root node down to the
# farthest leaf node.


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2


# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

from typing import Optional
import importlib
bt = importlib.import_module("lc-binary-tree")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if root is None:
            return 0

        max_left_height = self.maxDepth(root.left)
        max_right_height = self.maxDepth(root.right)
        return max(max_left_height, max_right_height) + 1

if __name__ == "__main__":
    root = bt.build_tree([3,9,20,None,None,15,7])
    print(Solution().maxDepth(root))
    root = bt.build_tree([1, None,2])
    print(Solution().maxDepth(root))

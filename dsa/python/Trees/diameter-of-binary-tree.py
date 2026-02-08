# 543. Diameter of Binary Tree

# Given the root of a binary tree, return the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path
# between any two nodes in a tree. This path may or may not pass through the
# root. The length of a path between two nodes is represented by the number of
# edges between them.

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def rMaxDiameter(n: TreeNode):  # DFS Post order
            nonlocal ans

            if not n:
                return 0

            lh = rMaxDiameter(n.left)
            rh = rMaxDiameter(n.right)
            ans = max(ans, lh + rh)  # Node specific statements
            return 1 + max(lh, rh)

        rMaxDiameter(root)
        return ans


if __name__ == "__main__":
    root = bt.build_tree([1, 2, 3, 4, 5])
    print(Solution().diameterOfBinaryTree(root))
    root = bt.build_tree([1, 2])
    print(Solution().diameterOfBinaryTree(root))

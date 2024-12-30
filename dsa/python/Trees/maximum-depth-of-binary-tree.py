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

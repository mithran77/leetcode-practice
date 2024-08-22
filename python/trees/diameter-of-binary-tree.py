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
        self.res = 0

        def maxHeight(node: TreeNode | None) -> int:
            if node is None:
                return 0

            lh = maxHeight(node.left)
            rh = maxHeight(node.right)
            self.res = max(self.res, lh+rh)
            return 1 + max(lh, rh)
        maxHeight(root)

        return self.res

if __name__ == "__main__":
    root = bt.build_tree([1,2,3,4,5])
    print(Solution().diameterOfBinaryTree(root))
    root = bt.build_tree([1,2])
    print(Solution().diameterOfBinaryTree(root))

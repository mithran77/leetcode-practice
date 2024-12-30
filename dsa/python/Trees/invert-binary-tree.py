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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Base case
        if root is None:
            return None

        # Swap L&R
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

if __name__ == "__main__":
    root = bt.build_tree([4,2,7,1,3,6,9])
    root = Solution().invertTree(root)
    bt.printLevelOrder(root)

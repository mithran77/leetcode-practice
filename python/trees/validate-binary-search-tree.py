from typing import Optional
import importlib
bt = importlib.import_module("lc-binary-tree")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node: TreeNode | None, minVal: float, maxVal: float) -> bool:
            # Base cases
            if not node:
                return True
            if not (minVal < node.val and node.val < maxVal):
                return False
            # Recursive case
            return (
                valid(node.left, minVal, node.val)
                and valid(node.right, node.val, maxVal)
            )

        return valid(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    root = bt.build_tree([2,1,3])
    print(Solution().isValidBST(root))
    root = bt.build_tree([5,1,4,None,None,3,6])
    print(Solution().isValidBST(root))


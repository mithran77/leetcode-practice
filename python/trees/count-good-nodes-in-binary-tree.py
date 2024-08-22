from typing import Optional, List
import importlib
bt = importlib.import_module("lc-binary-tree")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfsGoodNodes(node: TreeNode|None, maxVal):
            if not node:
                return 0
            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            maxVal = max(maxVal, node.val)
            res += dfsGoodNodes(node.left, maxVal)
            res += dfsGoodNodes(node.right, maxVal)

            return res

        return dfsGoodNodes(root, root.val)

if __name__ == "__main__":
    root = bt.build_tree([3,1,4,3,None,1,5])
    print(Solution().goodNodes(root))
    root = bt.build_tree([3,3,None,4,2])
    print(Solution().rightSideView(root))
    root = bt.build_tree([1])
    print(Solution().rightSideView(root))

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
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     res = []

    #     def inOrder(node: TreeNode|None, res):
    #         if not node:
    #             return
    #         inOrder(node.left, res)
    #         res.append(node.val)
    #         inOrder(node.right, res)

    #     inOrder(root, res)
    #     return res[k-1]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.kVal = float('inf')

        def inOrder(node: TreeNode|None):
            if not node:
                return
            inOrder(node.left)
            self.count += 1
            if self.count == k:
                self.kVal = node.val
                return
            inOrder(node.right)

        inOrder(root)
        return self.kVal


if __name__ == "__main__":
    root = bt.build_tree([3,1,4,None,2])
    print(Solution().kthSmallest(root, 1))
    root = bt.build_tree([5,3,6,2,4,None,None,1])
    print(Solution().kthSmallest(root, 3))

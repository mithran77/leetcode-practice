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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = bt.TreeNode(preorder[0])
        mid = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

if __name__ == "__main__":
    print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))
    print(Solution().buildTree([-1], [-1]))

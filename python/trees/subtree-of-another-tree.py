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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base cases

        # If sub tree is None
        if not subRoot:
            return True
        # root is None, subRoot exists
        if not root:
            return False
        # Same Trees
        if self.isSameTree(root, subRoot):
            return True

        # Recursive case
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )            

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or (p.val != q.val):
            return False

        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right) 
        )

if __name__ == "__main__":
    p = bt.build_tree([1,2,3])
    q = bt.build_tree([1,2,3])
    print(Solution().isSameTree(p, q))
    p = bt.build_tree([1,2])
    q = bt.build_tree([1,None,2])
    print(Solution().isSameTree(p, q))
    p = bt.build_tree([1,2,1])
    q = bt.build_tree([1,1,2])
    print(Solution().isSameTree(p, q))

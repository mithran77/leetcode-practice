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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases

        # if Both None: True
        if not p and not q:
            return True

        # if Either None or Value mismatch: False
        if not p or not q or (p.val != q.val):
            return False

        # Recursive case
        # if l==r: True; else: False
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
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

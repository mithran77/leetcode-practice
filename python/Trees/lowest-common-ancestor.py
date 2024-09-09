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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while True:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur.val

if __name__ == "__main__":
    root = bt.build_tree([6,2,8,0,4,7,9,None,None,3,5])
    print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(8)))
    root = bt.build_tree([6,2,8,0,4,7,9,None,None,3,5])
    print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))
    root = bt.build_tree([2,1])
    print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(1)))


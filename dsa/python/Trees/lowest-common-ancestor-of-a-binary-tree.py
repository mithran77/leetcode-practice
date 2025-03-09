# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the
# lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

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
        self.lca = root

        def rLca(node)->bool:
            # bcs
            if node is None:
                return False
            
            left = rLca(node.left)
            right = rLca(node.right)

            cur = node == p or node == q

            if (cur + left + right) >= 2:
                self.lca = node
            
            return left or right or cur


        rLca(root)
        return self.lca

if __name__ == "__main__":
    root = bt.build_tree([6,2,8,0,4,7,9,None,None,3,5])
    print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(8)))
    root = bt.build_tree([6,2,8,0,4,7,9,None,None,3,5])
    print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))
    root = bt.build_tree([2,1])
    print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(1)))


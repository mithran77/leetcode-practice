# 230. Kth Smallest Element in a BST

# Given the root of a binary search tree, and an integer k, return the kth
# smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104

# Follow up: If the BST is modified often (i.e., we can do insert and delete
# operations) and you need to find the kth smallest frequently, how would you
# optimize?


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
        count = 0
        k_val = float('inf')

        def inOrder(node: TreeNode | None):
            nonlocal count, k_val

            if not node:
                return
            inOrder(node.left)
            count += 1
            if count == k:
                k_val = node.val
                return
            inOrder(node.right)

        inOrder(root)
        return k_val


if __name__ == "__main__":
    root = bt.build_tree([3, 1, 4, None, 2])
    print(Solution().kthSmallest(root, 1))
    root = bt.build_tree([5, 3, 6, 2, 4, None, None, 1])
    print(Solution().kthSmallest(root, 3))

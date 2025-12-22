# 124. Binary Tree Maximum Path Sum

# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any
# non-empty path.

# Example 1:

# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3
# with a path sum of 2 + 1 + 3 = 6.


# Example 2:

# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7
# with a path sum of 15 + 20 + 7 = 42.

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

from typing import Optional
import importlib
bt = importlib.import_module("lc-binary-tree")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         self.max_sum = root.val

#         def postOrder(node):
#             if not node:
#                 return 0

#             l = postOrder(node.left)
#             if l < 0:
#                 l = 0
#             r = postOrder(node.right)
#             if r < 0:
#                 r = 0

#             self.max_sum = max(self.max_sum, node.val + l + r)

#             return node.val + max(l, r)

#         postOrder(root)
#         return self.max_sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def rMaxWeightedHeight(n: TreeNode):
            # DFS Postorder
            if not n:
                return 0

            lwh = rMaxWeightedHeight(n.left)
            rwh = rMaxWeightedHeight(n.right)
            path_sum = n.val + lwh + rwh
            self.ans = max(self.ans, path_sum)

            wh = n.val + max(lwh, rwh)
            if wh < 0:
                return 0
            else:
                return wh

        rMaxWeightedHeight(root)
        return self.ans


if __name__ == "__main__":
    root = bt.build_tree([1, 2, 3])
    print(Solution().maxPathSum(root))
    root = bt.build_tree([-10, 9, 20, None, None, 15, 7])
    print(Solution().maxPathSum(root))

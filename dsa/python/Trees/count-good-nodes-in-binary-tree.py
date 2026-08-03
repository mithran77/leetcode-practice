# 1448. Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named
# good if in the path from root to X there are no nodes
# with a value greater than X.

# Return the number of good nodes in the binary tree.

# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path
# starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.


# Example 2:
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because
# "3" is higher than it.

# Example 3:
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

# Constraints:

# The number of nodes in the binary tree is in the
# range [1, 10^5].
# Each node's value is between [-10^4, 10^4].


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

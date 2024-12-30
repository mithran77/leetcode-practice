from typing import List, Optional
from collections import deque
import importlib
bt = importlib.import_module("lc-binary-tree")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preOrderDFS(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            preOrderDFS(node.left)
            preOrderDFS(node.right)

        preOrderDFS(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def preOrderDFS():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = preOrderDFS()
            node.right = preOrderDFS()
            return node

        return preOrderDFS()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# if __name__ == "__main__":
#     root = bt.build_tree([3,9,20,None,None,15,7])
#     print(Solution().levelOrder(root))
#     root = bt.build_tree([1])
#     print(Solution().levelOrder(root))
#     root = bt.build_tree([])
#     print(Solution().levelOrder(root))

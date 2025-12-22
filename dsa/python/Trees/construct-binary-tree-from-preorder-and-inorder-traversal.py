# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.

# Example 1:

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


from typing import Optional, List
import importlib
bt = importlib.import_module("lc-binary-tree")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def buildTree(
#         self, preorder: List[int], inorder: List[int]
#     ) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None

#         root = bt.TreeNode(preorder[0])
#         mid = inorder.index(root.val)

#         root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

#         return root


class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        node = TreeNode(preorder[0])
        pivot = inorder.index(node.val)

        print("node.left", pivot, preorder[1:pivot+1], inorder[:pivot])
        node.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        print("node.right", pivot, preorder[pivot+1:], inorder[pivot+1:])
        node.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])

        return node


if __name__ == "__main__":
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
    print(Solution().buildTree([-1], [-1]))

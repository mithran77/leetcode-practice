# 145. Binary Tree Postorder Traversal

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]

# Output: [3,2,1]

# Explanation:

# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,6,7,5,2,9,8,3,1]

# Explanation:

# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # Recursive
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []

#         def dfs(n):
#             if not n:
#                 return

#             dfs(n.left)
#             dfs(n.right)
#             res.append(n.val)

#         dfs(root)
#         return res

# Iterative
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        st = deque([root])

        while st:
            n = st.pop()
            
        
        return res

if __name__ == '__main__':
    res = Solution()
    print(res.postorderTraversal(root = [1,None,2,3]))
    print(res.postorderTraversal(root = [1,2,3,4,5,None,8,None,None,6,7,9]))
    print(res.postorderTraversal(root = []))
    print(res.postorderTraversal(root = [1]))

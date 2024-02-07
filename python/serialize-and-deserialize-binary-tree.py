# 297. Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits 
# so that it can be stored in a file or memory buffer, or transmitted across a network connection 
# link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how 
# your serialization/deserialization algorithm should work. You just need to ensure that a binary 
# tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You 
# do not necessarily need to follow this format, so please be creative and come up with different 
# approaches yourself.

# Example 1:

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if not node:
                res.append('None')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        # Convert to list
        vals = data.split(',')
        # Handle None and cast int
        nodes = iter((None if val == 'None' else TreeNode(int(val)) for val in vals))
        root = next(nodes)
        q = deque([root])

        while q:
            node = q.popleft()
            left = next(nodes)
            if left:
                node.left = left
                q.append(left)
            right = next(nodes)
            if right:
                node.right = right
                q.append(right)

        return root


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()

    ans = deser.deserialize(ser.serialize([1,2,3,None,None,4,5]))
    print(ans)

    ans = deser.deserialize(ser.serialize([]))
    print(ans)

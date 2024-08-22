from typing import Optional, List
import importlib
import collections
bt = importlib.import_module("lc-binary-tree")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            rSide = None
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rSide:
                res.append(rSide.val)

        return res

if __name__ == "__main__":
    root = bt.build_tree([1,2,3,None,5,None,4])
    print(Solution().rightSideView(root))
    root = bt.build_tree([1,None,3])
    print(Solution().rightSideView(root))
    root = bt.build_tree([0,1,2,None,3,4,None,None,5,9,None,None,6,10,None])
    print(Solution().rightSideView(root))

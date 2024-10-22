# https://neetcode.io/problems/count-connected-components
# Count Connected Components
# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b]
# means that there is an edge between node a and node b in the graph.
#
# The nodes are numbered from 0 to n - 1.
#
# Return the total number of connected components in that graph.
#
# Example 1:
#
# Input:
# n=3
# edges=[[0,1], [0,2]]
#
# Output:
# 1
# Example 2:
#
# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]
#
# Output:
# 2
# Constraints:
#
# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2
#
#
#
from typing import List

# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         # Create parent
#         par = [ i for i in range(n) ]
#         rank = [1] * n

#         def findRootParent(v):
#             res = v

#             while res != par[res]:
#                 par[res] = par[par[res]]
#                 res = par[res]

#             return res

#         def union(v1, v2):
#             p1, p2 = findRootParent(v1), findRootParent(v2)

#             if p1 == p2:
#                 return 0

#             if rank[p2] > rank[p1]: # Ensure tree height ~1
#                 par[p1] = p2
#                 rank[p2] += rank[p1]
#             else:
#                 par[p2] = p1
#                 rank[p1] += rank[p2]

#             return 1

#         res = n
#         for v1, v2 in edges:
#             res -= union(v1, v2)

#         return res


class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x: int):
        y = self.f.get(x, x)
        if y != x:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x: int, y: int):
        self.f[self.findParent(x)] = self.findParent(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for x, y in edges:
            dsu.union(x, y)
        return len(set(dsu.findParent(x) for x in range(n)))


if __name__ == '__main__':
    ans = Solution()
    print(ans.countComponents(n=3, edges=[[0,1], [0,2]]))
    print(ans.countComponents(n=6, edges=[[0,1], [1,2], [2,3], [4,5]]))


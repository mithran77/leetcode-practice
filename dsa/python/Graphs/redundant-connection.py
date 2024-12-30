# 684. Redundant Connection

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
# return the answer that occurs last in the input.

# Example 1:

# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

from typing import List
from collections import defaultdict

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         # Create complete adjacency list
#         adj = defaultdict(list)
#         for v1, v2 in edges:
#             adj[v1].append(v2)
#             adj[v2].append(v1)

#         # Remove edges in reverse
#         for i in range(len(edges)-1, 0, -1):
#             v1, v2 = edges[i]
#             adj[v1].remove(v2)
#             if adj[v1] == []:
#                 del adj[v1]
#             adj[v2].remove(v1)
#             if adj[v2] == []:
#                 del adj[v2]
#             if self.isValidTree(adj.copy()):
#                 return [v1, v2]

#     def isValidTree(self, neighbors):

#         visit = set()
#         def dfs(node, p):
#             # BC
#             if node in visit:
#                 return False

#             visit.add(node)
#             for n in neighbors[node]:
#                 if n == p:
#                     continue
#                 if not dfs(n, node):
#                     return False

#             return True

#         return dfs(1, 0) and (len(visit) == len(neighbors))

# Union Find
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)] 
        rank = [1] * (len(edges) + 1)

        def find(v):
            p = parent[v]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p] 

            return p

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for v1, v2 in edges:
            if not union(v1, v2):
                return  [v1, v2]


if __name__ == '__main__':
    res = Solution()
    print(res.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))
    # print(res.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))
    # print(res.findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]))

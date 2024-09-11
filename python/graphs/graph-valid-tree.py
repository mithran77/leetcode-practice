#
# Valid Tree
# https://neetcode.io/problems/valid-tree
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.
#
# Example 1:
#
# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
#
# Output:
# true
# Example 2:
#
# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
#
# Output:
# false
# Note:
#
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] 
# and thus will not appear together in edges.
# Constraints:
#
# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2
#

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # Create adjacency list
        adj = { i : [] for i in range(n) }
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = set()

        def dfs(val: int, prev: int) -> bool:
            # BC Detect cycle
            if val in visited:
                return False

            visited.add(val)
            # RC
            for nei in adj[val]:
                if nei == prev:
                    continue
                if not dfs(nei, val):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)

if __name__ == '__main__':
    ans = Solution()
    print(ans.validTree(n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(ans.validTree(n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))


# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume 
# all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List
from collections import deque


# class Solution:

#     def numIslands(self, grid: List[List[str]]) -> int:

#         # Base case
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         islands = 0

#         def bfs(r, c):

#             q = deque()
#             q.append((r, c))
#             visited.add((r, c))

#             while len(q):
#                 row, col = q.popleft()
#                 directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#                 for dr, dc in directions:
#                     adjx, adjy = row + dr, col + dc
#                     if ( adjx in range(rows) and adjy in range(cols) and grid[adjx][adjy] == "1" and (adjx, adjy) not in visited ):
#                         q.append((adjx, adjy))
#                         visited.add((adjx, adjy))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     bfs(r, c)
#                     islands += 1

#         return islands


# # DFS
# class Solution:

#     def numIslands(self, grid: List[List[str]]) -> int:

#         if not grid:
#             return 0

#         ROWS, COLS = len(grid), len(grid[0])
#         islands = 0
#         visited = set()

#         def dfs(r, c):
#             if (r not in range(ROWS) or
#                 c not in range(COLS) or
#                 grid[r][c] == "0" or
#                 (r, c) in visited):
#                 return

#             visited.add((r, c))
#             directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
#             for dr, dc in directions:
#                 dfs(r + dr, c + dc)

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     islands += 1
#                     dfs(r, c)

#         return islands

# BFS
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while(q):
                row, col = q.popleft()
                neighbours = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                for dr, dc in neighbours:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visited and
                        grid[r][c] == "1"):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands

if __name__ == '__main__':
    ans = Solution()
    print(ans.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))
    print(ans.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]))


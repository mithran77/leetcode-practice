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
from collections import deque as queue


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        # Base case
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):

            q = queue()
            q.append((r, c))
            visited.add((r, c))

            while len(q):
                row, col = q.popleft()
                directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for dr, dc in directions:
                    adjx, adjy = row + dr, col + dc
                    if ( adjx in range(rows) and adjy in range(cols) and grid[adjx][adjy] == "1" and (adjx, adjy) not in visited ):
                        q.append((adjx, adjy))
                        visited.add((adjx, adjy))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

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


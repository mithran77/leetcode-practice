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

# Recursive DFS
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visited or
                grid[r][c] != "1"):
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands

# Iterative BFS
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            visited.add((r, c))
            q = deque((r, c))

            while q:
                r, c = q.popleft()
                neighbours = [(r - 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
                for r, c in neighbours:
                    if (r not in range(ROWS) or
                        c not in range(COLS)):
                        continue
                    if (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
                

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

# Time & Space Complexity 
# Time complexity: O(m ∗ n) 
# Space complexity: O(m ∗ n)
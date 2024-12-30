# 286. Walls and Gates

# You are given an m x n grid rooms initialized with these three possible values.

#     -1 A wall or an obstacle.
#     0 A gate.
#     INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the
# distance to a gate is less than 2147483647.

# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example 1:

# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Example 2:

# Input: rooms = [[-1]]
# Output: [[-1]]

# Constraints:

#     m == rooms.length
#     n == rooms[i].length
#     1 <= m, n <= 250
#     rooms[i][j] is -1, 0, or 231 - 1.
#
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
# Islands and Treasure

# m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is one of {-1, 0, 2147483647}



from typing import List

# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         # For each Treasure
#         ROWS, COLS = len(grid), len(grid[0])
#         visited = set()

#         def dfs(r, c, dist):
#             # Cannot be traversed or treasure chest
#             if (r not in range(ROWS) or
#                 c not in range(COLS) or 
#                 grid[r][c] == -1 or
#                 (grid[r][c] == 0 and dist > 0) or
#                 (r, c) in visited):
#                 return

#             if dist > 0:
#                 grid[r][c] = min(grid[r][c], dist)
#             visited.add((r, c))
#             # Visit neighbours and update
#             dfs(r + 1, c, dist + 1)
#             dfs(r - 1, c, dist + 1)
#             dfs(r, c + 1, dist + 1)
#             dfs(r, c - 1, dist + 1)
#             visited.remove((r, c))

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == 0:
#                     dfs(r, c, 0)

#         return grid

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def addCell(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        # Add all 0s to q
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                # Add neighbours to visit and q
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

        return grid


if __name__ == '__main__':
    ans = Solution()
    print(ans.islandsAndTreasure(grid = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]))
    print(ans.islandsAndTreasure(grid = [[-1]]))
    print(ans.islandsAndTreasure(grid = [
        [0,-1],
        [2147483647,2147483647]
    ]))


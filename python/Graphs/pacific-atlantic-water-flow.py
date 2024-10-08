# 417. Pacific Atlantic Water Flow

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean 
# touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where 
# heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, 
# east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water 
# can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from 
# cell (ri, ci) to both the Pacific and Atlantic oceans.

# Example 1:

# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Example 2:

# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]

# Constraints:

# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

from typing import List
from collections import deque as queue


# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         ROWS, COLS = len(heights), len(heights[0])
#         atl, pac = set(), set()

#         def dfs(r, c, visit):
#             visit.add((r, c))
#             q = queue()
#             q.append((r, c))

#             while len(q):
#                 r, c = q.pop()
#                 directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#                 for dr, dc in directions:
#                     row = r + dr
#                     col = c + dc
#                     if  row >= 0 and row < ROWS and\
#                         col >= 0 and col < COLS and\
#                         heights[row][col] >= heights[r][c] and\
#                         (row, col) not in visit:
#                         q.append((row, col))
#                         visit.add((row, col))

#         for r in range(ROWS):
#             dfs(r, 0, pac)
#             dfs(r, COLS - 1, atl)

#         for c in range(COLS):
#             dfs(0, c, pac)
#             dfs(ROWS - 1, c, atl)

#         ans = []
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if (r, c) in atl and (r, c) in pac:
#                     ans.append([r, c])

#         return ans


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                heights[r][c] < prevHeight or
                (r, c) in visited):
                return

            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if heights[r][c] in pac and heights[r][c] in atl:
                    res.append(heights[r][c])

        return res

if __name__ == '__main__':
    ans = Solution()
    print(ans.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(ans.pacificAtlantic([[2,1],[1,2]]))
    print(ans.pacificAtlantic([[1]]))


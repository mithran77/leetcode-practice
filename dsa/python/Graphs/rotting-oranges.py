# 994. Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        # Collect 2's in q & 1's count in fresh
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        # BFS for each 2's
        minutes = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in neighbours:
                    if (nr not in range(ROWS) or
                        nc not in range(COLS) or
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1


if __name__ == '__main__':
    ans = Solution()
    print(ans.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
    print(ans.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
    print(ans.orangesRotting(grid = [[0,2]]))


# Time & Space Complexity
# Time complexity:  O(m∗n)
# Space complexity:  O(m∗n)
# Where  m is the number of rows and n is the number of columns in the grid.

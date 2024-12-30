# 130. Surrounded Regions

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none
# of the region cells are on the edge of the board.
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.


from typing import List

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         ROWS, COLS = len(board), len(board[0])

#         def dfs(r, c):

#             if (r not in range(ROWS) or
#                 c not in range(COLS) or
#                 (r, c) in visit or
#                 board[r][c] == "X"):
#                 return
#             if ((r == 0 or r == ROWS - 1 or 
#                  c == 0 or c == COLS - 1) and
#                 board[r][c] == "O"):
#                 self.surrounded = False

#             visit.add((r, c))
#             dfs(r + 1, c)
#             dfs(r - 1, c)
#             dfs(r, c + 1)
#             dfs(r, c - 1)


#         for r in range(ROWS):
#             for c in range(COLS):
#                 if board[r][c] == "O":
#                     self.surrounded = True
#                     visit = set()
#                     dfs(r, c)
#                     # Mark x if surrounded
#                     if self.surrounded:
#                         for r, c in visit:
#                             board[r][c] = "X"

#         return board

# # Visit set
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         ROWS, COLS = len(board), len(board[0])
#         visit = set()

#         def dfs(r, c):
#             if (r not in range(ROWS) or
#                 c not in range(COLS) or
#                 (r, c) in visit or
#                 board[r][c] == "X"):
#                 return

#             visit.add((r, c))
#             dfs(r + 1, c)
#             dfs(r - 1, c)
#             dfs(r, c + 1)
#             dfs(r, c - 1)

#         # 1st and last col
#         for c in (0, COLS - 1):
#             for r in range(ROWS):
#                 dfs(r, c)

#         # 1st and last row
#         for r in (0, ROWS - 1):
#             for c in range(COLS):
#                 dfs(r, c)

#         # Mark all surrounded
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if (r, c) not in visit and board[r][c] == "O":
#                     board[r][c] = "X"

#         return board

# Space optimized
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != "O"):
                return

            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1st and last col
        for c in (0, COLS - 1):
            for r in range(ROWS):
                dfs(r, c)

        # 1st and last row
        for r in (0, ROWS - 1):
            for c in range(COLS):
                dfs(r, c)

        # Mark all surrounded
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

        return board


if __name__ == '__main__':
    ans = Solution()
    print(ans.solve(board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]))
    # print(ans.solve(board = [["X"]]))
    # print(ans.solve(board = [
    #     ["X","O","O","X","X","X","O","X","O","O"],
    #     ["X","O","X","X","X","X","X","X","X","X"],
    #     ["X","X","X","X","O","X","X","X","X","X"],
    #     ["X","O","X","X","X","O","X","X","X","O"],
    #     ["O","X","X","X","O","X","O","X","O","X"],
    #     ["X","X","O","X","X","O","O","X","X","X"],
    #     ["O","X","X","O","O","X","O","X","X","O"],
    #     ["O","X","X","X","X","X","O","X","X","X"],
    #     ["X","O","O","X","X","O","X","X","O","O"],
    #     ["X","X","X","O","O","X","O","X","X","O"]
    # ]))


# 51. N-Queens

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]

# Constraints:

# 1 <= n <= 9

from typing import List

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         queens = []
#         # Create 3 sets to check if queens can attack each other
#         cols, pos_diag, neg_diag = set(), set(), set()

#         board = [['.'] * n for _ in range(n)] 

#         def backtrack(r):
#             # BC
#             if r == n:
#                 copy = [''.join(row) for row in board]
#                 queens.append(copy)
#             # RC
#             else:
#                 for c in range(n):
#                     if (c in cols or (r + c) in pos_diag or (r - c) in neg_diag):
#                         continue

#                     # Bookkeeping
#                     cols.add(c)
#                     pos_diag.add(r + c)
#                     neg_diag.add(r - c)
#                     board[r][c] = 'Q'

#                     backtrack(r + 1)

#                     # Bookkeeping
#                     cols.remove(c)
#                     pos_diag.remove(r + c)
#                     neg_diag.remove(r - c)
#                     board[r][c] = '.'

#         backtrack(0)
#         return queens


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        board = [
            ["." for _ in range(n)]
            for _ in range(n)
        ]

        def valid_placement(row, col):
            # Invalidate early for column and diagonals
            # for already placed rows

            # Column
            for r in range(row):
                if board[r][col] == 'Q':
                    return False

            # 1st diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1

            # 2nd diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            return True

        def solve(row: int, col: int):
            if row == n: # Deep copy the board & return
                deep_copy = []
                for r in range(n):
                    deep_copy.append(''.join(board[r]))
                queens.append(deep_copy)
                return

            for c in range(n):
                if valid_placement(row, c):
                    board[row][c] = 'Q' # Place
                    solve(row+1, col)
                    board[row][c] = '.' # Remove

        solve(row=0, col=0)

        return queens

if __name__ == '__main__':
    res = Solution()
    print(res.solveNQueens(n = 4))
    print(res.solveNQueens(n = 1))


from typing import List
import collections

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Hashmap of hashsets
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9): # Rows
            for c in range(9): # Columns
                v = board[r][c]
                if v == ".":
                    continue
                if (v in rows[r] or
                    v in cols[c] or
                    v in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(v)
                cols[c].add(v)
                squares[(r // 3, c // 3)].add(v)

        return True

if __name__ == '__main__':
    res = Solution()
    print(res.isValidSudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]))
    print(res.isValidSudoku([
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]))

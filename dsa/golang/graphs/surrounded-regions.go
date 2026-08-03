/*
    130. Surrounded Regions

    You are given an m x n matrix board containing
    letters 'X' and 'O', capture regions that are
    surrounded:

    Connect: A cell is connected to adjacent cells
    horizontally or vertically.
    Region: To form a region connect every 'O' cell.
    Surround: The region is surrounded with 'X'
    cells if you can connect the region with 'X'
    cells and none of the region cells are on the
    edge of the board. A surrounded region is
    captured by replacing all 'O's with 'X's in the
    input matrix board.

    Example 1:
    Input: board = [["X","X","X","X"],["X","O","O","X"],
    ["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],
    ["X","X","X","X"],["X","O","X","X"]]

    Explanation:
    In the above diagram, the bottom region is not
    captured because it is on the edge of the board and
    cannot be surrounded.

    Example 2:
    Input: board = [["X"]]
    Output: [["X"]]

    Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.

*/


func solve(board [][]byte)  {
    rows, cols := len(board), len(board[0])

    var dfs func(r, c int)
    dfs = func(r, c int) {
        if (r < 0 || c < 0 ||
            r >= rows || c >= cols ||
            board[r][c] != 'O') {
            return
        }

        board[r][c] = 'C'
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
    }

    for c := range cols {
        if board[0][c] == 'O' {
            dfs(0,c)
        }
        if board[rows-1][c] == 'O'{
            dfs(rows-1,c)
        }
    }

    for r := range rows {
        if board[r][0] == 'O' {
            dfs(r,0)
        }
        if board[r][cols-1] == 'O'{
            dfs(r,cols-1)
        }
    }

    for r := range rows {
        for c := range cols {
            if board[r][c] == 'O' {
                board[r][c] = 'X'
            }
            if board[r][c] == 'C' {
                board[r][c] = 'O'
            }
        }
    }
}
/*
    994. Rotting Oranges

    You are given an m x n grid where each cell can have
    one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally
    adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse
    until no cell has a fresh orange. If this is impossible,
    return -1.

    Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

    Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2,
    column 0) is never rotten, because rotting only happens
    4-directionally.

    Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at
    minute 0, the answer is just 0.

    Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.

*/

func orangesRotting(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    q := [][]int{}

    for r := range rows {
        for c := range cols {
            if grid[r][c] == 2 {
                q = append(q, []int{r, c})
            }
        }
    }

    nei := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    level := 0
    for len(q) > 0 {        
        qLen := len(q)
        level++

        for range qLen {
            r, c := q[0][0], q[0][1]
            q = q[1:]
            for _, n := range nei {
                nr, nc := r + n[0], c + n[1]
                if (0 <= nr && nr < rows) && (0 <= nc && nc < cols) && (grid[nr][nc] == 1) {
                    q = append(q, []int{nr, nc})
                    grid[nr][nc] = 2
                }
            }
        }
    }

    for r := range rows {
        for c := range cols {
            if grid[r][c] == 1 {
                return -1
            }
        }
    }

    if level > 0 {
        return level - 1
    }
    return level
}
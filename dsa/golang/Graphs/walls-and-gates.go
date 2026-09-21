/*
    286. Walls and Gates

    You are given an m x n grid rooms initialized with these
    three possible values.

        -1 A wall or an obstacle.
        0 A gate.
        INF Infinity means an empty room. We use the value
    231 - 1 = 2147483647 to represent INF as you may assume
    that the distance to a gate is less than 2147483647.

    Fill each empty room with the distance to its nearest
    gate. If it is impossible to reach a gate, it should be
    filled with INF.

    Example 1:

    Input: rooms = [[2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1], [0,-1,2147483647,2147483647]]
    Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

    Example 2:

    Input: rooms = [[-1]]
    Output: [[-1]]

    Constraints:

        m == rooms.length
        n == rooms[i].length
        1 <= m, n <= 250
        rooms[i][j] is -1, 0, or 231 - 1.

    #############################################################
    #############################################################
    #############################################################
    Islands and Treasure

    m×n 2D grid initialized with these three possible values:

    -1 - A water cell that can not be traversed.
    0 - A treasure chest.
    INF - A land cell that can be traversed. We use the
    integer 2^31 - 1 = 2147483647 to represent INF.
    Fill each land cell with the distance to its nearest
    treasure chest. If a land cell cannot reach a treasure
    chest than the value should remain INF.

    Assume the grid can only be traversed up, down, left,
    or right.

    Example 1:

    Input: [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
    ]

    Output: [
    [3,-1,0,1],
    [2,2,1,-1],
    [1,-1,2,-1],
    [0,-1,3,4]
    ]
    Example 2:

    Input: [
    [0,-1],
    [2147483647,2147483647]
    ]

    Output: [
    [0,-1],
    [1,2]
    ]
    Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    grid[i][j] is one of {-1, 0, 2147483647}
*/

func islandsAndTreasure(grid [][]int) {
    rows, cols := len(grid), len(grid[0])

    q := [][]int{}
    for r := range rows {
        for c := range cols {
            if grid[r][c] == 0 {
                q = append(q, []int{r,c})
            }
        }
    }

    var isValid func(r, c int) bool
    isValid = func(r, c int) bool {
        return (0 <= r && r < rows) &&
           (0 <= c && c < cols) &&
           (grid[r][c] == 2147483647)
    }

    nei := [][]int{{-1,0}, {1,0}, {0,-1}, {0,1}}
    level := 1
    for len(q) > 0 {
        qLen := len(q)

        for range qLen {
            r, c := q[0][0], q[0][1]
            q = q[1:]

            for _, n := range nei {
                nr, nc := r + n[0], c + n[1]
                if isValid(nr, nc) {
                    grid[nr][nc] = level
                    q = append(q, []int{nr, nc})
                }
            }

        }

        level++
    }

}

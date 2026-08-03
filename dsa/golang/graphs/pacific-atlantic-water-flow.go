/*

    417. Pacific Atlantic Water Flow

    There is an m x n rectangular island that borders
    both the Pacific Ocean and Atlantic Ocean. The
    Pacific Ocean touches the island's left and top
    edges, and the Atlantic Ocean touches the island's
    right and bottom edges.

    The island is partitioned into a grid of square
    cells. You are given an m x n integer matrix heights
    where heights[r][c] represents the height above sea
    level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water
    can flow to neighboring cells directly north, south, 
    east, and west if the neighboring cell's height is
    less than or equal to the current cell's height. Water 
    can flow from any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where
    result[i] = [ri, ci] denotes that rain water can flow
    from cell (ri, ci) to both the Pacific and Atlantic oceans.

    Example 1:

    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],
    [6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    Example 2:

    Input: heights = [[2,1],[1,2]]
    Output: [[0,0],[0,1],[1,0],[1,1]]

    Constraints:

    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 105

*/

func pacificAtlantic(heights [][]int) [][]int {
    rows, cols := len(heights), len(heights[0])
    pac, atl := make(map[[2]int]bool), make(map[[2]int]bool)

    var dfs func(r, c, prevHeight int, visited map[[2]int]bool)
    dfs = func(r, c, prevHeight int, visited map[[2]int]bool) {
        if (r < 0 || c < 0 ||
            r >= rows || c >= cols ||
            heights[r][c] < prevHeight ||
            visited[[2]int{r, c}]) {
            return
        }

        visited[[2]int{r, c}] = true
        dfs(r-1, c, heights[r][c], visited)
        dfs(r+1, c, heights[r][c], visited)
        dfs(r, c-1, heights[r][c], visited)
        dfs(r, c+1, heights[r][c], visited)

    }

    for c := range cols {
        dfs(0, c, heights[0][c], pac)
        dfs(rows-1, c, heights[rows-1][c], atl)
    }

    for r := range rows {
        dfs(r, 0, heights[r][0], pac)
        dfs(r, cols-1, heights[r][cols-1], atl)
    }

    res := [][]int{}
    for r := range rows {
        for c := range cols {
            if pac[[2]int{r,c}] && atl[[2]int{r,c}] {
                res = append(res, []int{r,c})
            }
        }
    }
    return res
}
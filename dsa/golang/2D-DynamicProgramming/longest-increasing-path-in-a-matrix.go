/*

    329. Longest Increasing Path in a Matrix

    Given an m x n integers matrix, return
    the length of the longest increasing
    path in matrix.

    From each cell, you can either move in
    four directions: left, right, up, or down.
    You may not move diagonally or move
    outside the boundary
    (i.e., wrap-around is not allowed).

    Example 1:
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing
    path is [1, 2, 6, 9].

    Example 2:
    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing
    path is [3, 4, 5, 6]. Moving diagonally
    is not allowed.

    Example 3:
    Input: matrix = [[1]]
    Output: 1

    Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 231 - 1

*/

func longestIncreasingPath(matrix [][]int) int {
	rows, cols, longest := len(matrix), len(matrix[0]), 0
    dp := make([][]int, rows)
    for r := range rows {
        dp[r] = slices.Repeat([]int{-1}, cols)
    }

    var dfs func(r, c, prev int) int
    dfs = func(r, c, prev int) int {
        if r < 0 || r >= rows || c < 0 || c >= cols || matrix[r][c] <= prev {
            return 0
        }

        if dp[r][c] != -1 {
            return dp[r][c]
        }

        dp[r][c] = 1 + max(
            dfs(r - 1, c, matrix[r][c]),
            dfs(r + 1, c, matrix[r][c]),
            dfs(r, c - 1, matrix[r][c]),
            dfs(r, c + 1, matrix[r][c]),
        )
        return dp[r][c]
    }

	for r := range rows {
		for c := range cols {
            longest = max(longest, dfs(r, c, -1))
		}
	}

    return longest
}


/*

    54. Spiral Matrix

    Given an m x n matrix, return
    all elements of the matrix in
    spiral order.

    Example 1:
    Input: matrix = [[1,2,3],[4,5,6],
    [7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],
    [9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

    Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

*/

func spiralOrder(matrix [][]int) []int {
    res := []int{}

    rStart, cStart := 0, 0
    rEnd, cEnd := len(matrix) - 1, len(matrix[0]) - 1

    for rStart <= rEnd && cStart <= cEnd {
        // Right
        for c := cStart; c <= cEnd; c++ {
            res = append(res, matrix[rStart][c])
        }
        rStart++

        // Down
        for r := rStart; r <= rEnd; r++ {
            res = append(res, matrix[r][cEnd])
        }
        cEnd--

        // Left
        if rStart <= rEnd {
            for c := cEnd; c >= cStart; c-- {
                res = append(res, matrix[rEnd][c])
            }
            rEnd--
        }

        // Up
        if cStart <= cEnd {
            for r := rEnd; r >= rStart; r-- {
                res = append(res, matrix[r][cStart])
            }
        }

        cStart++
    }

    return res
}

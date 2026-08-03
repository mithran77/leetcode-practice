/*
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two
properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the
previous row. Given an integer target, return true if target is in matrix
or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

*/

// func searchMatrix(matrix [][]int, target int) bool {
//     ROWS, COLS := len(matrix), len(matrix[0])
//     l, r := -1, ROWS * COLS

//     for (l + 1) != r {
//         mid := l + ((r - l) / 2)
//         if (matrix[mid / COLS][mid % COLS] == target) {
//             return true
//         } else if (matrix[mid / COLS][mid % COLS] < target) {
//             l = mid
//         } else {
//             r = mid
//         }
//     }

//     return false
// }

func searchMatrix(matrix [][]int, target int) bool {
    rows, cols := len(matrix), len(matrix[0])

    if target < matrix[0][0] || target > matrix[rows-1][cols-1] {
        return false
    }
    l, r := -1, rows

    for l + 1 != r {
        m := l + (r - l) / 2
        if matrix[m][0] == target {
            return true
        } else if matrix[m][0] > target {
            r = m
        } else {
            l = m
        }
    }

    row := l
    l, r = -1, cols

    for l + 1 != r {
        m := l + (r - l) / 2
        if matrix[row][m] == target {
            return true
        } else if matrix[row][m] > target {
            r = m
        } else {
            l = m
        }
    }

    return false
}

func main() {
	fmt.Println(searchMatrix([][]int{[1,3,5,7],[10,11,16,20],[23,30,34,60]}, 3))
    fmt.Println(searchMatrix([][]int{[1,3,5,7],[10,11,16,20],[23,30,34,60]}, 13))
}

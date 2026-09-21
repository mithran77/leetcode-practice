/*

	73. Set Matrix Zeroes

	Given an m x n integer matrix matrix,
	if an element is 0, set its entire row
	and column to 0's.

	You must do it in place.

	Example 1:
	Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
	Output: [[1,0,1],[0,0,0],[1,0,1]]

	Example 2:
	Input: matrix = [[0,1,2,0],[3,4,5,2],
	[1,3,1,5]]
	Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
	

	Constraints:
	m == matrix.length
	n == matrix[0].length
	1 <= m, n <= 200
	-231 <= matrix[i][j] <= 231 - 1


	Follow up:
	A straightforward solution using O(mn)
	space is probably a bad idea.
	A simple improvement uses O(m + n)
	space, but still not the best solution.
	Could you devise a constant space solution?

*/

// Brute Force
func setZeroes(matrix [][]int)  {
    m, n := len(matrix), len(matrix[0])

    mask := make([][]int, m)
    for r := range m {
        mask[r] = slices.Repeat([]int{1}, n)
    }

    markRow := func (r int) {
        for c := range n {
            mask[r][c] = 0
        }
    }

    markCol := func(c int) {
        for r := range m {
            mask[r][c] = 0
        }
    }

    for r := range m {
        for c := range n {
            if matrix[r][c] == 0 {
                markRow(r); markCol(c)
            }
        }
    }

    for r := range m {
        for c := range n {
            // if mask[r][c] == 0 {
            //     matrix[r][c] = 0
            // }
			matrix[r][c] *= mask[r][c]
        }
    }

}


// Optimized - single row and col arrays
func setZeroes(matrix [][]int)  {
    m, n := len(matrix), len(matrix[0])

    rows := slices.Repeat([]int{1}, m)
    cols := slices.Repeat([]int{1}, n)

    for r := range m {
        for c := range n {
            if matrix[r][c] == 0 {
                rows[r] = 0; cols[c] = 0
            }
        }
    }

    for r := range rows {
        for c := range n {
            if rows[r] == 0 || cols[c] == 0 {
                matrix[r][c] = 0
            }
        }
    }
}

// In Place
// In Place
func setZeroes(matrix [][]int)  {
    m, n := len(matrix), len(matrix[0])

    // rows := slices.Repeat([]int{1}, m)
    // cols := slices.Repeat([]int{1}, n)

	zeroRow := 1
    for r := range m {
        for c := range n {
            if matrix[r][c] == 0 {
                if r == 0 {
					zeroRow = 0
				} else {
					matrix[r][0] = 0
				}
				matrix[0][c] = 0
            }
        }
    }

	// Mark Rows
	for r := 1; r < m; r++ {
		if matrix[r][0] == 0 {
			for c := 1; c < n; c++ {
				matrix[r][c] = 0
			}
		}
    }

	// Mark Cols
	for c := 1; c < n; c++ {
		if matrix[0][c] == 0 {
			for r := 1; r < m; r++ {
				matrix[r][c] = 0
			}
		}
    }

	if matrix[0][0] == 0 {
		for r := 1; r < m; r++ {
			matrix[r][0] = 0
		}
	}

	if zeroRow == 0 {
		for c := 0; c < n; c++ {
			matrix[0][c] = 0
		}
	}

}

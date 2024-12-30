# 74. Search a 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # BS on ROWS
        s, e = 0, ROWS - 1
        while s <= e:
            m = (s + ((e - s) // 2))
            if target < matrix[m][0]:
                e = m - 1
            elif target > matrix[m][COLS - 1]:
                s = m + 1
            else:
                break

        if not (s <= e): # While loop failed (not within bounds of rows)
            return False
        row = (s + ((e - s) // 2)) # Initialize row to m

        # BS on COLS
        l, r = 0, COLS - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False

if __name__ == '__main__':
    res = Solution()
    print(res.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(res.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
    print(res.searchMatrix(matrix = [[1,3]], target = 3))


# Time:  O(log m) * O(log n) = O(log (m*n))
# Space: O(1)
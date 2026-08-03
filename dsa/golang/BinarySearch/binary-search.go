/*
    704. Binary Search

    Given an array of integers nums which is sorted in ascending order, and an
    integer target, write a function to search target in nums. If target exists,
    then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
    Example 2:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

    Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
*/

package main

import "fmt"

// func search(nums []int, target int) int {
// 	i, j := 0, len(nums)-1
// 	var mid int
// 	for i <= j {
// 		mid = (i + j) / 2
// 		if target > nums[mid] {
// 			i = mid + 1
// 		} else if target == nums[mid] {
// 			return mid
// 		} else {
// 			j = mid - 1
// 		}
// 	}
// 	return -1
// }

func search(nums []int, target int) int {
    start, end := -1, len(nums)

    for (start + 1) != end {
        m := start + (end - start) / 2
        if nums[m] == target {
            return m
        } else if target > nums[m]  {
            start = m
        } else {
            end = m
        }
    }

    return -1
}

func main() {
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 9))
}

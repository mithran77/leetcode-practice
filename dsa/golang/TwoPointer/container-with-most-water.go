/*
# 11. Container With Most Water
#
# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0) and
# (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that
# the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
# Example 1:
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
#
# Example 2:
#
# Input: height = [1,1]
# Output: 1
#
#
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
*/


// Trick to remember when both pointers are at equal heights
// Whichever pointer moves, the container height is bound
// by the current height, if a greater height is found, the
// other pointer will move to accomodate

func maxArea(height []int) int {
    max_area := 0
    l, r := 0, len(height) - 1

    for l < r {
        area := min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)

        if height[l] < height[r] {
            l++
        } else {
            r--
        }
    }

    return max_area
}


func main() {
    fmt.Println(maxArea([]int{1,8,6,2,5,4,8,3,7}))
    fmt.Println(maxArea([]int{1,1}))
}

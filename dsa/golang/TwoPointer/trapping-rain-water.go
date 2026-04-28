/*
# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it
# can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented
# by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

*/

// Prefix-Suffix Max
func trap(height []int) int {
    rain_water := 0
    capacity := make([]int, len(height))

    left_max := 0
    for i, h := range(height) {
        capacity[i] = left_max
        left_max = max(left_max, h)
    }

    right_max := 0
    for i := len(height)-1; i > -1; i-- {
        capacity[i] = min(capacity[i], right_max)
        right_max = max(right_max, height[i])
    }

    for i, h := range(height) {
        if capacity[i] > h {
            rain_water += capacity[i] - h
        }
    }

    return rain_water
}

// 2P
func trap(height []int) int {
    l, r := 0, len(height) - 1
    // At the start and end indices, water cannot be stored
    // as it will spill to the sides, because there is only
    // one side to the container
    left_max, right_max := height[l], height[r]
    water := 0
    
    for l < r {
        if left_max < right_max {
            l++
            if left_max > height[l] {
                water += left_max - height[l]
            }
            left_max = max(left_max, height[l])
        } else {
            r--
            if right_max > height[r] {
                water += right_max - height[r]
            }
            right_max = max(right_max, height[r])
        }
    }

    return water
}


func main() {
    fmt.Println(trap([]int{0,1,0,2,1,0,1,3,2,1,2,1}))
    fmt.Println(trap([]int{4,2,0,3,2,5}))
}

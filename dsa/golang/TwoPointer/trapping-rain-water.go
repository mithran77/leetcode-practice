/*

    42. Trapping Rain Water

    Given n non-negative integers representing
    an elevation map where the width of each bar
    is 1, compute how much water it can trap after
    raining.

    Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black
    section) is represented by
    array [0,1,0,2,1,0,1,3,2,1,2,1].
    In this case, 6 units of rain water (blue
    section) are being trapped.

    Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

    Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105

*/

// Prefix-Suffix Max
// func trap(height []int) int {
//     rain_water := 0
//     capacity := make([]int, len(height))

//     left_max := 0
//     for i, h := range(height) {
//         capacity[i] = left_max
//         left_max = max(left_max, h)
//     }

//     right_max := 0
//     for i := len(height)-1; i > -1; i-- {
//         capacity[i] = min(capacity[i], right_max)
//         right_max = max(right_max, height[i])
//     }

//     for i, h := range(height) {
//         if capacity[i] > h {
//             rain_water += capacity[i] - h
//         }
//     }

//     return rain_water
// }

func trap(height []int) int {
    lMax, rMax := slices.Repeat([]int{0}, len(height)), slices.Repeat([]int{0}, len(height))
    trapped := 0

    cMax := 0
    for i := 0; i < len(height); i++ {
        cMax = max(cMax, height[i])
        lMax[i] = cMax
    }
    cMax = 0
    for i := len(height)-1; i > -1 ; i-- {
        cMax = max(cMax, height[i])
        rMax[i] = cMax
    }

    for i, h := range height {
        trapped += min(lMax[i], rMax[i]) - h
    }

    return trapped
}

// 2P
func trap(height []int) int {
    l, r := 0, len(height) - 1
    // At the start and end indices, water cannot be stored
    // as it will spill to the sides, because there is only
    // one side to the container
    lMax, rMax := height[l], height[r]
    water := 0

    for l < r {
        if lMax < rMax {
            l++
            if lMax > height[l] {
                water += lMax - height[l]
            } else {
                lMax = max(lMax, height[l])
            }
        } else {
            r--
            if rMax > height[r] {
                water += rMax - height[r]
            } else {
                rMax = max(rMax, height[r])
            }
        }
    }

    return water
}


func main() {
    fmt.Println(trap([]int{0,1,0,2,1,0,1,3,2,1,2,1}))
    fmt.Println(trap([]int{4,2,0,3,2,5}))
}

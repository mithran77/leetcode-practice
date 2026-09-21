/*

    55. Jump Game

    You are given an integer array nums. You are initially
    positioned at the array's first index, and each element
    in the array represents your maximum jump length at that
    position.

    Return true if you can reach the last index, or false
    otherwise.

    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps
    to the last index.

    Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter
    what. Its maximum jump length is 0, which makes it
    impossible to reach the last index.

    Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 105

*/

// BFS - TLE
func canJump(nums []int) bool {
    queue := []int{0}
    seen := map[int]struct{}{0: {}}

    maxReach := 0

    for len(queue) > 0 {
        levelSize := len(queue)

        for range levelSize {

            pos := queue[0]
            queue = queue[1:]

            for reach := range nums[pos] {
                next := pos + reach + 1
                if _, ok := seen[next]; next < len(nums) && !ok {
                    maxReach = max(maxReach, next)
                    seen[next] = struct{}{}
                    queue = append(queue, next)
                }
            }

        }
    }

    return maxReach == len(nums)-1
}

// DP
// func canJump(nums []int) bool {

//     dp := slices.Repeat([]int{-1}, len(nums))

//     var rCanJump func(step int) int
//     rCanJump = func(step int) int {
//         if step >= len(nums) - 1 {
//             return 1
//         }

//         if dp[step] != -1 {
//             return dp[step]
//         }

//         dp[step] = 0
//         for i := range nums[step] {
//             if rCanJump(step + i + 1) == 1 {
//                 dp[step] = 1
//                 break
//             }
//         }

//         return dp[step]
//     }

//     return rCanJump(0) == 1
// }

func canJump(nums []int) bool {
    dp := slices.Repeat([]int{-1}, len(nums))

    var reach func(step int) int
    reach = func(step int) int {
        if dp[step] != -1 {
            return dp[step]
        }

        if step == len(nums) - 1 {
            return len(nums) - 1
        }

        best := min(step+nums[step], len(nums) - 1) // furthest a single jump lands
        for i := range nums[step] {
            next := step + i + 1
            best = max(best, reach(next))
            if best == len(nums) - 1 {
                break
            }
        }

        dp[step] = best
        return best
    }

    return reach(0) == len(nums) - 1
}

// Greedy
func canJump(nums []int) bool {

    maxReach := 0
    for i, n := range nums {
        if i > maxReach {
            return false
        }
        reach := i + n
        maxReach = max(maxReach, reach)
        if maxReach >= len(nums) - 1 {
            return true
        }
    }

    return false
}


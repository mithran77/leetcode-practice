/*

    45. Jump Game II

    You are given a 0-indexed array of integers nums
    of length n. You are initially positioned at nums[0].

    Each element nums[i] represents the maximum length
    of a forward jump from index i. In other words,
    if you are at nums[i], you can jump to any
    nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n
    Return the minimum number of jumps to reach
    nums[n - 1]. The test cases are generated such
    that you can reach nums[n - 1].

    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach
    the last index is 2. Jump 1 step from index 0 to 1,
    then 3 steps to the last index.

    Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2

    Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].

*/

// BFS

func jump(nums []int) int {
    queue := []int{0}
    seen := map[int]struct{}{0: {}}

    jumps := 0
    for len(queue) > 0 {
        levelSize := len(queue)
        for range levelSize {
            pos := queue[0]
            queue = queue[1:]
            if pos == len(nums)-1 {
                return jumps
            }
            for reach := range nums[pos] {
                next := pos + reach + 1
                if _, ok := seen[next]; next < len(nums) && !ok {
                    seen[next] = struct{}{}
                    queue = append(queue, next)
                }
            }
        }
        jumps++
    }

    return jumps
}

// DP

func jump(nums []int) int {    
    dp := slices.Repeat([]int{-1}, len(nums) + 1)

    var rJump func(step int) int
    rJump = func(step int) int {
        if step >= len(nums) - 1 {
            return 0
        }
        if dp[step] != -1 {
            return dp[step]
        }
        minJumps := 10001
        for i := range nums[step] {
            minJumps = min(minJumps, 1 + rJump(step + i + 1))
        }
        dp[step] = minJumps
        return dp[step]
    }

    return rJump(0)
}

// Greedy
func jump(nums []int) int {
    l, r := 0, 0
    jumps := 0

    for r < len(nums) - 1 {
        farthest := 0
        for l <= r {
            farthest = max(farthest, l + nums[l])
            l++
        }
        jumps++
        l, r = r + 1, farthest
    }

    return jumps
}
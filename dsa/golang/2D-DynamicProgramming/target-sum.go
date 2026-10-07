/*

    494. Target Sum

    You are given an integer array
    nums and an integer target.

    You want to build an expression
    out of nums by adding one of the
    symbols '+' and '-' before each
    integer in nums and then concatenate
    all the integers.

    For example, if nums = [2, 1], you
    can add a '+' before 2 and a '-'
    before 1 and concatenate them to
    build the expression "+2-1".
    Return the number of different
    expressions that you can build, which
    evaluates to target.

    Example 1:
    Input: nums = [1,1,1,1,1],
    target = 3
    Output: 5
    Explanation: There are 5 ways to
    assign symbols to make the sum of nums
    be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3

    Example 2:
    Input: nums = [1], target = 1
    Output: 1

    Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000

*/

func findTargetSumWays(nums []int, target int) int {
    n := len(nums)
    dp := map[[2]int]int{}

    var rTargetSumWays func(i, total int) int
    rTargetSumWays = func(i, total int) int {
        if total == target && i == n  {
            return 1
        }
        if i >= n {
            return 0
        }

        key := [2]int{i, total}
        if val, exists := dp[key]; exists {
            return val
        }

        plus := rTargetSumWays(i + 1, total - nums[i])
        minus := rTargetSumWays(i + 1, total + nums[i])

        dp[key] = plus + minus

        return dp[key]
    }

    return rTargetSumWays(0, 0)
}


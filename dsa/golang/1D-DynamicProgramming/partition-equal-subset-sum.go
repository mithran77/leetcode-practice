/*

    416. Partition Equal Subset Sum

    Given an integer array nums, return
    true if you can partition the array
    into two subsets such that the sum
    of the elements in both subsets is
    equal or false otherwise.

    Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be
    partitioned as [1, 5, 5] and [11].

    Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be
    partitioned into equal sum subsets.


    Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 100

*/

// DP

func canPartition(nums []int) bool {
    sum := 0
    for _, n := range nums {
        sum += n
    }

    if sum % 2 != 0 {
        return false
    }

    dp := make([][]int, len(nums))
    for i := range len(nums) {
        dp[i] = slices.Repeat([]int{-1}, (sum / 2) + 1)
    }

    var rCanPartition func(i, req int) int
    rCanPartition = func(i, req int) int {
        if req == 0 {
            return 1
        }
        if req < 0 || i >= len(nums) {
            return 0
        }
        if dp[i][req] != -1 {
            return dp[i][req]
        }

        // Take
        take := rCanPartition(i + 1, req - nums[i])
        // Not Take
        skip := rCanPartition(i + 1, req)

        dp[i][req] = 0
        if take + skip > 0 {
            dp[i][req] = 1
        }

        return dp[i][req]
    }

    return rCanPartition(0, sum/2) == 1
}

/*

    300. Longest Increasing Subsequence

    Given an integer array nums, return
    the length of the longest strictly
    increasing subsequence.

    Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing
    subsequence is [2,3,7,101], therefore
    the length is 4.

    Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

    Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

    Constraints:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

    Follow up: Can you come up with ane
    algorithm that runs in O(n log(n))
    time complexity?

*/

func lengthOfLIS(nums []int) int {
    dp := slices.Repeat([]int{-1}, len(nums))

    var rLIS func(i int) int
    rLIS = func(i int) int {
        if dp[i] != -1 {
            return dp[i]
        }

        best := 1
        for j := i + 1; j < len(nums); j++ {
            if nums[i] < nums[j] {
                best = max(best, 1 + rLIS(j))
            }
        }

        dp[i] = best
        return dp[i]
    }

    longest := 0
    for i := range nums {
        longest = max(longest, rLIS(i))
    }

    return longest
}


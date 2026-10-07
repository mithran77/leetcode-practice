/*

    312. Burst Balloons

    You are given n balloons,
    indexed from 0 to n - 1.
    Each balloon is painted with
    a number on it represented
    by an array nums. You are
    asked to burst all the balloons.

    If you burst the ith balloon,
    you will get,
    nums[i - 1] * nums[i] * nums[i + 1]
    coins. If i - 1 or i + 1 goes out of
    bounds of the array, then treat
    it as if there is a balloon with
    a 1 painted on it.

    Return the maximum coins you can
    collect by bursting the balloons
    wisely. 

    Example 1:
    Input: nums = [3,1,5,8]
    Output: 167
    Explanation:
    nums = [3,1,5,8] --> [3,5,8]
    --> [3,8] --> [8] --> []
    coins =  3*1*5    +   3*5*8   +
    1*3*8  + 1*8*1 = 167

    Example 2:
    Input: nums = [1,5]
    Output: 10

    Constraints:
    n == nums.length
    1 <= n <= 300
    0 <= nums[i] <= 100

*/


// Brute Force
func maxCoins(nums []int) int {
    nums = append(nums, 1)
    nums = append([]int{1}, nums...)

    var dfs func(n []int) int
    dfs = func(n []int) int {
        if len(n) == 2 {
            return 0
        }

        maxCoin := 0
        for i := 1; i < len(n)-1; i++ {
            coins := n[i-1] * n[i] * n[i+1]

            subArray := []int{}
            subArray = append(subArray, n[:i]...)
            subArray = append(subArray, n[i+1:]...)

            coins += dfs(subArray)
            maxCoin = max(maxCoin, coins)
        }

        return maxCoin
    }

    return dfs(nums)
}


// 2D DP
func maxCoins(nums []int) int {
    nums = append(nums, 1)
    nums = append([]int{1}, nums...)

    dp := make([][]int, len(nums))
    for r := range len(nums) {
        dp[r] = slices.Repeat([]int{-1}, len(nums))
    }

    var dfs func(l, r int) int
    dfs = func(l, r int) int {
        if l > r {
            return 0
        }

        if dp[l][r] != -1 {
            return dp[l][r]
        }

        dp[l][r] = 0
        for i := l; i <= r; i++ {
            coins := nums[l-1] * nums[i] * nums[r+1]
            coins += dfs(i + 1, r)
            coins += dfs(l, i - 1)
            dp[l][r] = max(dp[l][r], coins)
        }

        return dp[l][r]
    }

    return dfs(1, len(nums)-2)
}


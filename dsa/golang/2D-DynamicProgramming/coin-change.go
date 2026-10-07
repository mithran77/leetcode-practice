/*

    322. Coin Change

    You are given an integer array
    coins representing coins of different
    denominations and an integer
    amount representing a total amount
    of money. Return the fewest number of
    coins that you need to make up that
    amount. If that amount of money cannot
    be made up by any combination of the
    coins, return -1. You may assume that
    you have an infinite number of each
    kind of coin.

    Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

    Example 2:
    Input: coins = [2], amount = 3
    Output: -1

    Example 3:
    Input: coins = [1], amount = 0
    Output: 0

    Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104

*/

// 2D DP
func coinChange(coins []int, amount int) int {
    dp := make([][]int, len(coins))
    for i := range len(coins) {
        dp[i] = slices.Repeat([]int{-1}, amount + 1)
    }

    var rCoinChange func(i, cur int) int
    rCoinChange = func(i, cur int) int {
        if i >= len(coins) || cur > amount {
            return math.MaxInt
        }
        if dp[i][cur] != -1 {
            return dp[i][cur]
        }
        if cur == amount {
            return 0
        }

        // Take
        take := rCoinChange(i, cur + coins[i])
        if take < math.MaxInt {
            take++
        }
        // No Take
        skip := rCoinChange(i + 1, cur)

        dp[i][cur] = min(take, skip)
        return dp[i][cur]
    }

    minCoins := rCoinChange(0, 0)
    if minCoins == math.MaxInt {
        return -1
    }
    return minCoins
}


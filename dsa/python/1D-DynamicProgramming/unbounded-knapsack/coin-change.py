# 322. Coin Change

# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the
# coins, return -1. You may assume that you have an infinite number of
# each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

from typing import List
from functools import cache

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [amount + 1] * (amount + 1)
#         dp[0] = 0

#         for a in range(1, amount + 1):
#             for c in coins:
#                 if a - c >= 0:
#                     dp[a] = min(dp[a], 1 + dp[a - c])
#         return dp[amount] if dp[amount] != amount + 1 else -1

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # dp = [-1] * (amount+1)
#         dp = {}

#         def rCoinChange(amount):
#             if amount not in dp:
#                 return dp[amount]
#             # BCs
#             if amount < 0:
#                 return float("inf")
#             if amount == 0:
#                 return 0

#             min_coins = float("inf")
#             for i in range(len(coins)):
#                 total = 1 + rCoinChange(amount - coins[i])
#                 min_coins = min(min_coins, total)

#             dp[amount] = min_coins
#             return min_coins

#         res = rCoinChange(amount)

#         if res == float("inf"):
#             return -1
#         else:
#             return res


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def rKnapsack(i, cur_amount):
            if cur_amount == amount:
                return 0
            if i == 0:
                return float("inf")

            if (cur_amount + coins[i-1]) > amount:
                return rKnapsack(i-1, cur_amount)
            else:
                pick = 1 + rKnapsack(i, cur_amount + coins[i-1])
                skip = rKnapsack(i-1, cur_amount)
                return min(pick, skip)

        min_coins = rKnapsack(len(coins), 0)
        if min_coins == float("inf"):
            return -1
        else:
            return min_coins


if __name__ == "__main__":
    ans = Solution()
    print(ans.coinChange(coins=[1, 2, 5], amount=11))
    print(ans.coinChange(coins=[2], amount=3))
    print(ans.coinChange(coins=[1], amount=0))

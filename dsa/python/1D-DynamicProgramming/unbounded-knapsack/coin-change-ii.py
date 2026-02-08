# 518. Coin Change II

# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that
# amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:
# Input: amount = 10, coins = [10]
# Output: 1

# Constraints:
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000


from typing import List
from functools import cache


# # TLE
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [
#             [-1] * (amount+1)
#             for _ in range(len(coins))
#         ]

#         def rChange(start, total):
#             if total > amount:
#                 return 0

#             if dp[start][total] != -1:
#                 return dp[start][total]

#             elif total == amount:
#                 return 1

#             result = 0
#             for i in range(start, len(coins)):
#                 result += rChange(i, total+coins[i])

#             dp[start][total] = result

#             return result

#         return rChange(0, 0)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def rKnapsack(i, cur_amount):
            if cur_amount == amount:
                return 1
            if i == 0:
                return 0

            if (cur_amount + coins[i-1]) > amount:
                return rKnapsack(i-1, cur_amount)
            else:
                pick = rKnapsack(i, cur_amount + coins[i-1])
                skip = rKnapsack(i-1, cur_amount)
                return pick + skip

        return rKnapsack(len(coins), 0)


if __name__ == "__main__":
    ans = Solution()
    print(ans.change(amount=5, coins=[1, 2, 5]))
    print(ans.change(amount=3, coins=[2]))
    print(ans.change(amount=10, coins=[10]))

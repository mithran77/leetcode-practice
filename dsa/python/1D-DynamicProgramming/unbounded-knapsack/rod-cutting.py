# https://www.geeksforgeeks.org/problems/rod-cutting0840/1

# Rod Cutting

# Given a rod of length n inches and an array price[], where
# price[i] denotes the value of a piece of length i. Your task
# is to determine the maximum value obtainable by cutting up the
# rod and selling the pieces.

# Note: n = size of price, and price[] is 1-indexed array.

# Example:

# Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]
# Output: 22
# Explanation: The maximum obtainable value is 22 by cutting in two
# pieces of lengths 2 and 6, i.e., 5 + 17 = 22.

# Input: price[] = [3, 5, 8, 9, 10, 17, 17, 20]
# Output: 24
# Explanation: The maximum obtainable value is 24 by cutting the rod
# into 8 pieces of length 1, i.e, 8*price[1] = 8*3 = 24.

# Input: price[] = [3]
# Output: 3
# Explanation: There is only 1 way to pick a piece of length 1.

# Constraints:
# 1 ≤ price.size() ≤ 103
# 1 ≤ price[i] ≤ 106

from functools import cache


class Solution:
    def cutRod(self, price):

        @cache
        def rKnapsack(i, cur_len):
            if i == 0:
                return 0

            if (cur_len + i) > len(price):
                return rKnapsack(i - 1, cur_len)
            else:
                pick = price[i-1] + rKnapsack(i, cur_len + i)
                skip = rKnapsack(i - 1, cur_len)
                return max(pick, skip)

        return rKnapsack(len(price), 0)


if __name__ == "__main__":
    res = Solution()
    print(res.cutRod(price=[1, 5, 8, 9, 10, 17, 17, 20]))
    print(res.cutRod(price=[3, 5, 8, 9, 10, 17, 17, 20]))
    print(res.cutRod(price=[3]))

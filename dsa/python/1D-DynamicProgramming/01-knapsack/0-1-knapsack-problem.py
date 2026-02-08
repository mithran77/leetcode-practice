# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

# 0 - 1 Knapsack Problem
# Difficulty: MediumAccuracy: 31.76%Submissions: 548K+Points: 4
# Given two arrays, val[] and wt[], where each element represents the
# value and weight of an item respectively, and an integer W representing
# the maximum capacity of the knapsack (the total weight it can hold).

# The task is to put the items into the knapsack such that the total value
# obtained is maximum without exceeding the capacity W.

# Note: You can either include an item completely or exclude it entirely —
# fractional selection of items is not allowed. Each item is available only
# once.

# Examples :

# Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]
# Output: 3
# Explanation: Choose the last item, which weighs 1 unit and has a value of 3.

# Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6]
# Output: 0
# Explanation: Every item has a weight exceeding the knapsack's capacity (3).

# Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3]
# Output: 80
# Explanation: Choose the third item (value 30, weight 2) and the last item
# (value 50, weight 3) for a total value of 80.
# Constraints:
# 1 ≤ val.size() = wt.size() ≤ 103
# 1 ≤ W ≤ 103
# 1 ≤ val[i] ≤ 103
# 1 ≤ wt[i] ≤ 103


class Solution:
    def knapsack(self, W, val, wt):
        dp = [
            [-1] * (W + 1)
            for _ in range(len(val)+1)
        ]

        def r01Knapsack(index, cur_weight):
            if dp[index][cur_weight] != -1:
                return dp[index][cur_weight]

            if index < 0 or cur_weight == 0:
                return 0

            if (cur_weight - wt[index-1]) < 0:  # not pick
                dp[index][cur_weight] = r01Knapsack(index - 1, cur_weight)
            else:
                pick = val[index-1] +\
                    r01Knapsack(index - 1, cur_weight - wt[index-1])
                skip = r01Knapsack(index - 1, cur_weight)
                dp[index][cur_weight] = max(pick, skip)

            return dp[index][cur_weight]

        return r01Knapsack(len(val) - 1, W)


if __name__ == "__main__":
    res = Solution()
    # print(res.knapsack(W=4, val=[1, 2, 3], wt=[4, 5, 1]))
    # print(res.knapsack(W=3, val=[1, 2, 3], wt=[4, 5, 6]))
    # print(res.knapsack(W=5, val=[10, 40, 30, 50], wt=[5, 4, 2, 3]))
    print(res.knapsack(W=7, val=[10, 8, 6], wt=[1, 7, 9]))

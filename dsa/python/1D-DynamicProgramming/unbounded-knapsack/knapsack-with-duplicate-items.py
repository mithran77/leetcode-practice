# https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1

# Knapsack with Duplicate Items

# Given a set of items, each with a weight and a value, represented by the
# array wt[] and val[] respectively. Also, a knapsack with a weight limit
# capacity. Your task is to fill the knapsack in such a way that we can get
# the maximum profit. Return the maximum profit.

# Note: Each item can be taken any number of times.

# Examples:

# Input: val[] = [1, 1], wt[] = [2, 1], capacity = 3
# Output: 3
# Explanation: The optimal choice is to pick the 2nd element 3 times.

# Input: val[] = [10, 40, 50, 70], wt[] = [1, 3, 4, 5], capacity = 8
# Output: 110
# Explanation: The optimal choice is to pick the 2nd element and the
# 4th element.

# Input: val[] = [6, 8, 7, 100], wt[] = [2, 3, 4, 5], capacity = 1
# Output: 0
# Explanation: We can't pick any element. Hence, total profit is 0.

# Constraints:
# 1 ≤ val.size() = wt.size() ≤ 1000
# 1 ≤ capacity ≤ 1000
# 1 ≤ val[i], wt[i] ≤ 100
from functools import cache


class Solution:
    def knapSack(self, val, wt, capacity):

        @cache
        def rKnapSack(i, cur_weight) -> int:
            if i == 0:
                return 0

            if (cur_weight+wt[i-1]) > capacity:
                return rKnapSack(i-1, cur_weight)
            else:
                pick = val[i-1] + rKnapSack(i, cur_weight+wt[i-1])
                skip = rKnapSack(i-1, cur_weight)
                return max(pick, skip)

        return rKnapSack(len(wt), 0)


if __name__ == "__main__":
    res = Solution()
    print(res.knapSack(val=[1, 1], wt=[2, 1], capacity=3))
    print(res.knapSack(val=[10, 40, 50, 70], wt=[1, 3, 4, 5], capacity=8))
    print(res.knapSack(val=[6, 8, 7, 100], wt=[2, 3, 4, 5], capacity=1))

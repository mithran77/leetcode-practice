# 746. Min Cost Climbing Stairs

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999


from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def rMinCost(i):
            # Base case, we are allowed to start at either step 0 or step 1
            if i <= 1:
                return 0
            if i in cache:
                return cache[i]

            down_one = cost[i-1] + rMinCost(i-1)
            down_two = cost[i-2] + rMinCost(i-2)
            cache[i] = min(down_one, down_two)

            return cache[i]

        return rMinCost(len(cost))

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         memo = [-1]*len(cost)
#         def rMinCost(i):
#             # BC
#             if i >= len(cost):
#                 return 0
#             if memo[i] != -1:
#                 return memo[i]
#             jump = cost[i] + rMinCost(i+2)
#             walk = cost[i] + rMinCost(i+1)
#             memo[i] = min(jump, walk)
#             return memo[i]

#         return min(rMinCost(0), rMinCost(1))

if __name__ == '__main__':
    res = Solution()
    print(res.minCostClimbingStairs(cost = [10,15,20]))
    print(res.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))

# https://www.geeksforgeeks.org/dsa/count-of-subsets-with-sum-equal-to-x/

# Perfect Sum Problem
# Difficulty: MediumAccuracy: 20.58%Submissions: 597K+Points: 4
# Given an array arr of non-negative integers and an integer target, the task
# is to count all subsets of the array whose sum is equal to the given target.

# Examples:

# Input: arr = [5, 2, 3, 10, 6, 8], target = 10
# Output: 3
# Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.
# Input: arr = [2, 5, 1, 4, 3], target = 10
# Output: 3
# Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to
# the target 10.
# Input: arr = [5, 7, 8], target = 3
# Output: 0
# Explanation: There are no subsets of the array that sum up to the target 3.
# Input: arr = [35, 2, 8, 22], target = 0
# Output: 1
# Explanation: The empty subset is the only subset with a sum of 0.
# Constraints:
# 1 ≤ arr.size() ≤ 103
# 0 ≤ arr[i] ≤ 103
# 0 ≤ target ≤ 103


class Solution:
    def perfectSum(self, arr, target):

        dp = [
            [-1] * (target+1)
            for _ in range(len(arr)+1)
        ]

        def rKnapsack(i, required):
            if dp[i][required] != -1:
                return dp[i][required]

            if i == 0:
                if required == 0:
                    return 1
                else:
                    return 0

            if (required - arr[i - 1]) < 0:
                dp[i][required] = rKnapsack(i - 1, required)
            else:
                pick = rKnapsack(i - 1, required - arr[i - 1])
                not_pick = rKnapsack(i - 1, required)
                dp[i][required] = pick + not_pick

            return dp[i][required]

        return rKnapsack(len(arr), target)


if __name__ == "__main__":
    res = Solution()
    print(res.perfectSum(arr=[5, 2, 3, 10, 6, 8], target=10))
    print(res.perfectSum(arr=[2, 5, 1, 4, 3], target=10))
    print(res.perfectSum(arr=[5, 7, 8], target=3))
    print(res.perfectSum(arr=[35, 2, 8, 22], target=0))
    print(res.perfectSum(arr=[0, 0, 1], target=1))

# Subset Sum Problem
# https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/


# Given an array of positive integers arr[] and a value sum,
# determine if there is a subset of arr[] with sum equal to given sum.

# Examples:

# Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
# Output: true
# Explanation: Here there exists a subset with target sum = 9, 4+3+2 = 9.

# Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
# Output: false
# Explanation: There is no subset with target sum 30.

# Input: arr[] = [1, 2, 3], sum = 6
# Output: true
# Explanation: The entire array can be taken as a subset, giving 1 + 2 + 3 = 6.

# Constraints:
# 1 <= arr.size() <= 200
# 1<= arr[i] <= 200
# 1<= sum <= 104


class Solution:
    def isSubsetSum(self, arr, sum):

        dp = [
            [-1] * (sum+1)
            for _ in range(len(arr)+1)
        ]

        def rKnapsack(i, required):
            if dp[i][required] != -1:
                return dp[i][required]

            if required == 0:
                return True
            if i == 0:
                return False

            if (required - arr[i-1]) < 0:
                dp[i][required] = rKnapsack(i-1, required)
            else:
                pick = rKnapsack(i-1, required-arr[i-1])
                not_pick = rKnapsack(i-1, required)
                dp[i][required] = pick or not_pick

            return dp[i][required]

        return rKnapsack(len(arr), sum)


if __name__ == "__main__":
    res = Solution()
    print(res.isSubsetSum(arr=[3, 34, 4, 12, 5, 2], sum=9))
    print(res.isSubsetSum(arr=[3, 34, 4, 12, 5, 2], sum=30))
    print(res.isSubsetSum(arr=[1, 2, 3], sum=6))

# https://leetcode.com/problems/partition-equal-subset-sum/

# 416. Partition Equal Subset Sum
# Given an integer array nums, return true if you can partition the array
# into two subsets such that the sum of the elements in both subsets is
# equal or false otherwise.

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = 0
        for n in nums:
            total += n
        if (total % 2) == 1:
            return False

        required = int(total / 2)
        dp = [
            [-1] * (required+1)
            for _ in range(len(nums)+1)
        ]

        def rKnapsack(i, required):
            if dp[i][required] != -1:
                return dp[i][required]
            if required == 0:
                return True
            if i == 0:
                return False

            if (required - nums[i-1]) < 0:
                dp[i][required] = rKnapsack(i-1, required)
            else:
                pick = rKnapsack(i-1, required-nums[i-1])
                not_pick = rKnapsack(i-1, required)
                dp[i][required] = (pick or not_pick)

            return dp[i][required]

        return rKnapsack(len(nums), required)


if __name__ == "__main__":
    res = Solution()
    print(res.canPartition(nums=[1, 5, 11, 5]))
    print(res.canPartition(nums=[1, 2, 3, 5]))

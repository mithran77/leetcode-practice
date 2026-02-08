# 494. Target Sum

# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+'
# and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
# and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which
# evaluates to target.

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums
# be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Example 2:
# Input: nums = [1], target = 1
# Output: 1

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

from typing import List
from functools import cache


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:

#         @cache
#         def rKnapsack(i, cur_sum):
#             if i == 0:
#                 if cur_sum == target:
#                     return 1
#                 else:
#                     return 0

#             plus = rKnapsack(i-1, cur_sum + nums[i-1])
#             minus = rKnapsack(i-1, cur_sum - nums[i-1])
#             return plus + minus

#         return rKnapsack(len(nums), 0)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        @cache
        def rKnapsack(i, cur_sum):
            if i == 0:
                if total - (2 * cur_sum) == target:
                    return 1
                else:
                    return 0

            pick = rKnapsack(i - 1, cur_sum + nums[i - 1])
            skip = rKnapsack(i - 1, cur_sum)
            return pick + skip

        return rKnapsack(len(nums), 0)


if __name__ == "__main__":
    res = Solution()
    print(res.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
    print(res.findTargetSumWays(nums=[1], target=1))

# 198. House Robber
# Medium
# Topics
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# 
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
from typing import List

# A. Recursive (top-down)
class Solution:
    def rob(self, nums: List[int]) -> int:

        def rRob(i):
            if i < 0:
                return 0

            return (max(nums[i] + rRob(i - 2), rRob(i - 1)))

        return rRob(len(nums) - 1)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         rob1, rob2 = 0, 0

#         for n in nums:
#             temp = max(rob1 + n, rob2)
#             rob1 = rob2
#             rob2 = temp

#         return rob2

if __name__ == '__main__':
    res = Solution()
    print(res.rob(nums = [1,2,3,1]))
    print(res.rob(nums = [2,7,9,3,1]))


# RT
# A. Recursive (top-down)
# nums = [1,2,3,1]
# rRob(3)
# max(nums[3] + rRob(1), rRob(2))
# max(1 + (max(nums[1] + rRob(-1), rRob(0))), rRob(2))
# rRob()
# rRob(3)
# 
# 1. Two Sum
# Easy
#
# 28304
#
# 907
#
# Add to List
#
# Share
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         arrayLength = len(nums)
#         for i in range(0, arrayLength - 1):
#             for j in range(i + 1, arrayLength):
#                 if (nums[i] + nums[j]) == target:
#                     return [i, j]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req_map = {}

        for i in range(len(nums)):
            required = target - nums[i]
            if req_map.get(nums[i], 'Not Present') == 'Not Present':
                req_map[required] = i
            else:
                return [req_map[nums[i]], i]


if __name__ == '__main__':
    res = Solution()
    print(res.maxArea([1,1]))
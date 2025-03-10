# 287. Find the Duplicate Number
# Medium
# Topics
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pass

if __name__ == '__main__':
    res = Solution()
    print(res.detectCycle(head = [3, 2, 0, -4], pos = 1))
    print(res.detectCycle(head = [1, 2], pos = 0))
    print(res.detectCycle(head = [1], pos = -1))

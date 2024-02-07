# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
#
#
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
#
# Input: nums = [1,1]
# Output: [2]
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
#
#
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
#
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Var Init
        missing_numbers = []
        orig_length = len(nums)
        nums = list(sorted(set(nums)))

        # Base case
        if (orig_length < 2) or (len(nums) == orig_length):
            return missing_numbers

        # Search missing within
        j = 0
        for i in range(1, orig_length + 1):
            try:
                if i == nums[j]:
                    j += 1
                else:
                    missing_numbers.append(i)
            except IndexError:
                missing_numbers.append(i)

        return missing_numbers


if __name__ == '__main__':
    res = Solution()
    print(res.maxArea([1,1]))
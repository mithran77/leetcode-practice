# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
# Example 1:
#
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:
#
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
# Example 4:
#
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
#
#
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
from typing import List


# class Solution: # WRONG SOLUTION, READ QUESTION PROPERLY
#     def missingNumber(self, nums: List[int]) -> int:
#         # Corner cases
#         if len(nums) == 1:
#             if nums[-1] == 0 or nums[-1] == (len(nums) - 1):
#                 return nums[-1] + 1
#             else:
#                 return nums[-1] - 1

#         nums = sorted(nums)

#         # Normal Cases
#         for i in range(1, len(nums)):
#             if i > 0 and (nums[i] != nums[i-1] + 1):
#                 return nums[i] - 1

#         return nums[-1] + 1


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         for i in range(0, len(nums)):
#             if nums[i] != i:
#                 return i
#         return i + 1



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i])
        return res

if __name__ == '__main__':
    res = Solution()
    print(res.missingNumber(nums = [3,0,1]))
    print(res.missingNumber(nums = [0,1]))
    print(res.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))
    print(res.missingNumber(nums = [0]))

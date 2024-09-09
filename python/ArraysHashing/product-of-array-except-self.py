# 238. Product of Array Except Self
#
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         # Base case
#         if len(nums) < 2:
#             return []

#         answer, running_product = [1], 1

#         # Prefix Loop
#         for i in range(1, len(nums)):
#             running_product *= nums[i-1]
#             answer.append(running_product)

#         running_product = 1

#         # Postfix Loop
#         for i in range(len(nums) - 2, -1, -1):
#             running_product *= nums[i+1]
#             answer[i] *= running_product

#         return answer


# # n2
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = [1] * len(nums)

#         for i in range(len(nums)):
#             tmp = nums[i]
#             nums[i] = 1
#             for j in range(len(nums)):
#                 output[i] *= nums[j]
#             nums[i] = tmp

#         return output

# n solution
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = [1] * len(nums)
#         ln = len(nums)
#         prod = 1

#         # Left side prod
#         for i in range(1, ln):
#             prod *= nums[i-1]
#             output[i] *= prod

#         prod = 1
#         # Right side
#         for i in range(ln - 2, -1, -1):
#             prod *= nums[i+1]
#             output[i] *= prod

#         return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix_prod = 1
        for i in range(1, len(nums)):
            prefix_prod *= nums[i-1]
            res[i] *= prefix_prod

        postfix_prod = 1
        for i in range(len(nums)-2, -1, -1):
            postfix_prod *= nums[i+1]
            res[i] *= postfix_prod

        return res


if __name__ == '__main__':
    res = Solution()
    print(res.productExceptSelf([1,2,3,4]))

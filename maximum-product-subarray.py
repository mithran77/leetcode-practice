# 152. Maximum Product Subarray

# Given an integer array nums, find a contiguous non-empty subarray within the array that 
# has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

from typing import List


# # Brute force
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         max_prod = nums[0]

#         for i in range(len(nums)):
#             tmp_prod = nums[i]
#             max_prod = max(tmp_prod, max_prod)
#             for j in range(i + 1, len(nums)):
#                 tmp_prod *= nums[j]
#                 max_prod = max(tmp_prod, max_prod)

#         return max_prod


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        min_curr, max_curr = 1, 1

        for n in nums:
            tmp = max_curr
            max_curr = max(max_curr * n, min_curr * n, n)
            min_curr = min(tmp * n, min_curr * n, n)

            res = max(max_curr, res)

        return res

if __name__ == '__main__':
    res = Solution()
    print(res.maxProduct([2,3,-2,4]))
    print(res.maxProduct([-2,0,-1]))
    print(res.maxProduct([0,2]))


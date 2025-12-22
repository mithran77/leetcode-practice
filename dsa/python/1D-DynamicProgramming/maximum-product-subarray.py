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


# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:

#         res = max(nums)
#         min_curr, max_curr = 1, 1

#         for n in nums:
#             tmp = max_curr
#             max_curr = max(max_curr * n, min_curr * n, n)
#             min_curr = min(tmp * n, min_curr * n, n)

#             res = max(max_curr, res)

#         return res

# # MLE
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:

#         memo = [
#             [nums[i]] * len(nums)
#             for i in range(len(nums))
#         ]
#         max_product = nums[0]
        
#         def maxMinProduct(n:int, prev_min:int, prev_max:int):
#             old_min = prev_min
#             cur_min = min(n, prev_min * n, prev_max * n)
#             cur_max = max(n, old_min * n, prev_max * n)

#             return cur_min, cur_max

#         for i in range(1, len(nums)):
#             memo[i][0], memo[i][1] = maxMinProduct(
#                 n=nums[i],
#                 prev_min=memo[i-1][0],
#                 prev_max=memo[i-1][1]
#             )
#             max_product = max(max_product, memo[i][1])

#         return max_product

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = [
            (-11, -11)
            for _ in range(len(nums))
        ]
        max_prod = nums[0]

        def rMaxProduct(i) -> tuple[int, int]:
            if i == 0:
                return nums[i], nums[i]

            if (memo[i][0], memo[i][1]) != (-11, -11):
                return memo[i]

            prev_min, prev_max = rMaxProduct(i-1)
            tmp_min = prev_min
            cur_min = min(nums[i], prev_min * nums[i], prev_max * nums[i])
            cur_max = max(nums[i], tmp_min * nums[i], prev_max * nums[i])

            memo[i] = (cur_min, cur_max)

            return cur_min, cur_max

        for i in range(len(nums)):
            max_prod = max(max_prod, rMaxProduct(i)[1])

        return max_prod

if __name__ == '__main__':
    res = Solution()
    print(res.maxProduct([2,3,-2,4]))
    print(res.maxProduct([-2,0,-1]))
    print(res.maxProduct([0,2]))


# 53. Maximum Subarray
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which 
# has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide 
# and conquer approach, which is more subtle.
#
# n2
from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         answer = nums[0]

#         for i, n in enumerate(nums):
#             running_sum = n
#             if answer < running_sum:
#                 answer = running_sum
#             for j in range(i+1, len(nums)):
#                 running_sum += nums[j]
#                 if answer < running_sum:
#                     answer = running_sum

#         return answer


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
        
#         maxSub = nums[0] #Initialize first number from array to maxSub 
#         curSum = 0 #initialize current sum to zero
        
#         for n in nums : #iterate through all array 
#             if curSum <0:
#                 curSum = 0 #if its -ve number reset sum to zero
            
#             curSum+=n #addition of current sum and array(nums) value
#             maxSub = max(maxSub,curSum) #returning 1st value is bigger than currentsum 
        
#         return maxSub


# # n3
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]

#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 sum = 0
#                 for k in range(i, j+1):
#                     sum += nums[k]
#                 max_sum = max(max_sum, sum)

#         return max_sum


# # n2 optimized using existing sum
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]

#         for i in range(len(nums)):
#             sum = 0
#             for j in range(i, len(nums)):
#                 sum += nums[j]
#                 max_sum = max(max_sum, sum)

#         return max_sum


# Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, sum = nums[0], 0

        for i in range(len(nums)):
            if sum < 0: # Move slow pointer if net is negative
                sum = 0
            sum += nums[i]
            max_sum = max(max_sum, sum)

        return max_sum


if __name__ == '__main__':
    res = Solution()
    print(res.maxSubArray([5,4,-1,7,8]))
    print(res.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
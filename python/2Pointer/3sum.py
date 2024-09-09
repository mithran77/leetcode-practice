# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
# that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []


# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         s = sorted(nums)        
#         output = set()
#         for k in range(len(s)):
#             target = -s[k]
#             i, j = k+1, len(s)-1
#             while i < j:
#                 sum_two = s[i] + s[j]
#                 if sum_two < target:
#                     i += 1
#                 elif sum_two > target:
#                     j -= 1
#                 else:
#                     output.add((s[k],s[i],s[j]))
#                     i += 1
#                     j -= 1
#         return output

# # Brute Force (Time Limit Exceeded)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         output = []
#         for i in range(len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 for k in range(j + 1, len(nums)):
#                     t = sorted([nums[i], nums[j], nums[k]])
#                     if (nums[i] + nums[j] + nums[k]) == 0 and t not in output:
#                         output.append(t)

#         return output


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         # Sort first
#         nums = sorted(nums)
#         output = []

#         for i, n in enumerate(nums):
#             if i > 0 and (n == nums[i-1]):
#                 continue

#             l, r = i + 1, len(nums) -1

#             while l < r:
#                 three_sum = n + nums[l] + nums[r]
#                 if three_sum < 0:
#                     l += 1
#                 elif three_sum > 0:
#                     r -= 1
#                 else:
#                     output.append([n, nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1

#         return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res

if __name__ == '__main__':
    res = Solution()
    print(res.threeSum([-1,0,1,2,-1,-4]))
    print(res.threeSum([0,1,1]))
    print(res.threeSum([0,0,0]))
    print(res.threeSum([]))
    print(res.threeSum([0]))
    # print(res.threeSum([0,0,0,0]))

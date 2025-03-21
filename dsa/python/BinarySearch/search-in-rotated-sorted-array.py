# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
# or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104
from typing import List


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             m = l + (r - l) // 2

#             if nums[m] == target:
#                 return m

#             # m in Left sorted array
#             if nums[l] <= nums[m]:
#                 if target < nums[l] or target > nums[m]:
#                     l = m + 1
#                 else:
#                     r = m - 1

#             # m in right sorted array
#             else:
#                 if target < nums[m] or target > nums[r]:
#                     r = m - 1
#                 else:
#                     l = m + 1

#         return -1







# Template based
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: # Left sorted
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            else: # nums[r] >= nums[m] Right sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m
        if nums[l] == target:
            return l

        return -1

if __name__ == '__main__':
    res = Solution()
    print(res.search([4,5,6,7,0,1,2], 0))
    print(res.search([4,5,6,7,0,1,2], 3))
    print(res.search([1], 0))


# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

from typing import List

# Template based
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         l, r = 0, len(nums) - 1

#         while l < r:
#             m = l + ((r - l) // 2)
#             if nums[r] > nums[m]:
#                 r = m
#             else:
#                 l = m + 1

#         if nums[l] == target:
#             return [l - 1, l]

#         return [-1, -1]



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        res = []

        if not nums:
            return [-1, -1]

        # Get left bound
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        if nums[l] != target:
            return [-1, -1]
        res.append(l)

        # Get right bound
        l, r = l, len(nums) - 1

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target and nums[m + 1] != target:
                r = m
            else:
                l = m + 1

        res.append(l)
        return res




if __name__ == '__main__':
    res = Solution()
    print(res.searchRange(nums = [5,7,7,8,8,10], target = 8))
    print(res.searchRange(nums = [5,7,7,8,8,10], target = 6))
    print(res.searchRange(nums = [], target = 0))


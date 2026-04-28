/*
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return
# false if every element is distinct.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         unique = []
#         for num in nums:
#             if num in unique:
#                 return True
#             else:
#                 unique.append(num)
#         return False


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         unique = set(nums)
#         if len(unique) == len(nums):
#             return False
#         return True


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:

#         hashset = set() # declaring hashset

#         for n in nums: # n is iterator
#             if n in hashset: # if n exists in hashset return true
#                 return True
#             hashset.add(n) # else add it to hashset
#         return False # duplicate not exist return false

# Iterating through a single hash set is a little faster (not in order of
# magnitude though)
#
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         unique = set(nums)
#         if len(unique) == len(nums):
#             return False
#         return True


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         int_count = {}

#         for n in nums:
#             int_count[n] = int_count.get(n, 0) + 1
#             if int_count[n] > 1:
#                 return True
#         return False
*/

package main

import "fmt"

// func containsDuplicate(nums []int) bool {
// 	var count = make(map[int]bool)
// 	for _, i := range nums {
// 		_, ok := count[i]
// 		if ok {
// 			return true
// 		} else {
// 			count[i] = true
// 		}
// 	}
// 	return false
// }


func containsDuplicate(nums []int) bool {
    contains := make(map[int]struct{}) // empty struct takes no space

    for _, n := range(nums) {
        if _, exists := contains[n]; exists {
            return true
        }
        contains[n] = struct{}{}
    }

    return false
}


func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
}

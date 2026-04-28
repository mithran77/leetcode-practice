/*

# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

*/

package main

import (
	"fmt"
)

// // BruteForce
// func twoSum(nums []int, target int) []int {
// 	for i := range nums {
// 		for j := i + 1; j < len(nums); j++ {
// 			if nums[j]+nums[i] == target {
// 				return []int{i, j}
// 			}
// 		}
// 	}
// 	return []int{}
// }

// // BruteForce + reqMap
// func twoSum(nums []int, target int) []int {
// 	required := map[int]int{}
// 	for i, v := range nums {
// 		required[i] = target - v
// 	}
// 	for i := range nums {
// 		for j := i + 1; j < len(nums); j++ {
// 			if nums[j] == required[i] {
// 				return []int{i, j}
// 			}
// 		}
// 	}
// 	return []int{}
// }

// // Sorting 2 pointer approach (WRONG)
// func twoSum(nums []int, target int) []int {
// 	sort.Ints(nums)

// 	for i, j := 0, len(nums)-1; i < j; i++ {
// 		if nums[i]+nums[j] > target {
// 			for ; nums[i]+nums[j] >= target; j-- {
// 				if nums[i]+nums[j] == target {
// 					return []int{i, j}
// 				}
// 			}
// 		}
// 	}
// 	return []int{}
// }

// // Two-pass Hash Table
// func twoSum(nums []int, target int) []int {
// 	required := map[int]int{}
// 	for i, v := range nums {
// 		required[v] = i
// 	}
// 	for i, v := range nums {
// 		complement := target - v
// 		if val, ok := required[complement]; ok {
// 			if val != i {
// 				return []int{i, val}
// 			}
// 		}
// 	}
// 	return []int{}
// }

// // One-pass Hash Table
// func twoSum(nums []int, target int) []int {
// 	hashmap := map[int]int{}
// 	for i, v := range nums {
// 		complement := target - v
// 		if val, ok := hashmap[complement]; ok {
// 			return []int{i, val}
// 		}
// 		hashmap[v] = i
// 	}
// 	return []int{}
// }


func twoSum(nums []int, target int) []int {
    complement := make(map[int]int)

    for j, n := range(nums) {
        if i, exists := complement[n]; exists {
            return []int{i, j}
        }
        complement[target - n] = j
    }

    return []int{-1, -1}
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}

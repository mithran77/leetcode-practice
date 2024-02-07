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

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}

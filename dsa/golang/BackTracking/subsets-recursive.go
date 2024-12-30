package main

import (
	"fmt"
)

func subsetsRecursive(nums []int) [][]int {
	res := [][]int{}

	subset := []int{}
	var bfs func(int)
	bfs = func(i int) {
		if i == len(nums) {
			dc := make([]int, len(subset))
			copy(dc, subset)
			res = append(res, dc)
			return
		}
		subset = append(subset, nums[i])
		bfs(i + 1)
		subset = subset[:len(subset)-1]
		bfs(i + 1)
	}
	bfs(0)
	return res
}

func main() {
	fmt.Println(subsetsRecursive([]int{1, 2, 3}))
	fmt.Println(subsetSumAny([]int{1, 2, 1}, 2))
	fmt.Println(subsetSumCount([]int{1, 2, 1}, 2))
}

func subsetSumAny(nums []int, n int) bool {

	subset := []int{}
	sum := 0
	var bfs func(int) bool
	bfs = func(i int) bool {
		if i == len(nums) {
			if n == sum {
				return true
			} else {
				return false
			}
		}
		subset = append(subset, nums[i])
		sum += nums[i]
		if bfs(i+1) == true {
			return true
		}
		subset = subset[:len(subset)-1]
		sum -= nums[i]
		if bfs(i+1) == true {
			return true
		}
		return false
	}
	return bfs(0)
}

func subsetSumCount(nums []int, n int) int {

	subset := []int{}
	sum := 0
	var bfs func(int) int
	bfs = func(i int) int {
		if i == len(nums) {
			if sum == n {
				return 1
			} else {
				return 0
			}
		}
		subset = append(subset, nums[i])
		sum += nums[i]
		l := bfs(i + 1)
		subset = subset[:len(subset)-1]
		sum -= nums[i]
		r := bfs(i + 1)
		return l + r
	}
	return bfs(0)
}

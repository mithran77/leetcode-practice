package main

import "fmt"

func search(nums []int, target int) int {
	i, j := 0, len(nums)-1
	var mid int
	for i <= j {
		mid = (i + j) / 2
		if target > nums[mid] {
			i = mid + 1
		} else if target == nums[mid] {
			return mid
		} else {
			j = mid - 1
		}
	}
	return -1
}

func main() {
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 9))
}

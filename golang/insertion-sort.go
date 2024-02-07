package main

import "fmt"

func insertionSort(nums []int) []int {
	if len(nums) < 2 {
		return nums
	}
	for i := 1; i < len(nums); i++ {
		tmp := nums[i]
		j := i - 1
		for j >= 0 && tmp < nums[j] {
			nums[j+1] = nums[j]
			j--
		}
		nums[j+1] = tmp
	}
	return nums
}

func main() {
	fmt.Println(insertionSort([]int{1, 3, 8, 2, 9, 2, 5, 6}))
}

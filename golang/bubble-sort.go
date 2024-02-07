package main

import "fmt"

func bubbleSort(nums []int) []int {
	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums)-1; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}
	return nums
}

func main() {
	fmt.Println(bubbleSort([]int{1, 3, 8, 2, 9, 2, 5, 6}))
}

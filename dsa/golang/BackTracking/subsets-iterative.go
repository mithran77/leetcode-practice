package main

import "fmt"

func subsetsIterative(nums []int) [][]int {
	res := [][]int{[]int{}}
	for i := 0; i < len(nums); i++ {
		currSize := len(res)
		for j := 0; j < currSize; j++ {
			new := append(res[j], nums[i])
			res = append(res, new)
		}
	}
	return res
}

func main() {
	fmt.Println(subsetsIterative([]int{1, 2, 3}))
}

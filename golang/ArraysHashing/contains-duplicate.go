package main

import "fmt"

func containsDuplicate(nums []int) bool {
	var count = make(map[int]bool)
	for _, i := range nums {
		_, ok := count[i]
		if ok {
			return true
		} else {
			count[i] = true
		}
	}
	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
}

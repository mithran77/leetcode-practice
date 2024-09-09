package main

import "fmt"

func topKFrequent(nums []int, k int) []int {
	var counts = map[int]int{}
	// max := nums[0]
	res := []int{nums[0]}
	for _, v := range nums {
		counts[v]++

		if counts[max] < counts[v] {
			max = v
		}
	}

	// delete(counts, max)

	// for i := 0; i < k; i++ {

	// }

	return res
}

func main() {
	fmt.Println([]int{1, 1, 1, 2, 2, 3}, 2)
}

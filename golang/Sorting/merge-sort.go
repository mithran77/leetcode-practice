package main

import "fmt"

//https://github.com/algorithms-go/merge-sort/blob/master/sort/merge.go
func merge(l, r []int) []int {
	a := make([]int, len(l)+len(r))
	i, j, k := 0, 0, 0
	// Sort in ascending order
	for i < len(l) && j < len(r) {
		if l[i] < r[j] {
			a[k] = l[i]
			i++
		} else {
			a[k] = r[j]
			j++
		}
		k++
	}

	// Append elements that were missed
	for i < len(l) {
		a[k] = l[i]
		i++
		k++
	}
	for j < len(r) {
		a[k] = r[j]
		j++
		k++
	}

	return a
}

func mergeSort(nums []int) []int {
	if len(nums) > 1 {
		m := len(nums) / 2
		l := nums[:m] //nums[0:m]
		r := nums[m:] //nums[m:len(nums)]
		nums = merge(mergeSort(l), mergeSort(r))
	}
	return nums
}

func main() {
	fmt.Println(mergeSort([]int{1, 3, 8, 2, 9, 2, 5, 6}))
}

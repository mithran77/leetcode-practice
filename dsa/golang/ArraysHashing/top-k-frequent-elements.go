/*
# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most
# frequent elements.
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
*/

package main

import "fmt"

// func topKFrequent(nums []int, k int) []int {
// 	var counts = map[int]int{}
// 	// max := nums[0]
// 	res := []int{nums[0]}
// 	for _, v := range nums {
// 		counts[v]++

// 		if counts[max] < counts[v] {
// 			max = v
// 		}
// 	}

// 	// delete(counts, max)

// 	// for i := 0; i < k; i++ {

// 	// }

// 	return res
// }

func topKFrequent(nums []int, k int) []int {

	freq := make(map[int]int)
	for _, n := range nums {
		freq[n]++
	}

	freq_buckets := make([][]int, len(nums)+1)
	for e, f := range freq {
		freq_buckets[f] = append(freq_buckets[f], e)
	}

    res := make([]int, 0, k)
	for _, elements := range slices.Backward(freq_buckets) {
		for _, e := range elements {
            if k == 0 {
                return res
            }
            res = append(res, e)
            k--
		}
	}

	return res

}

func main() {
	fmt.Println([]int{1, 1, 1, 2, 2, 3}, 2)
}

/*
	347. Top K Frequent Elements

	Given an integer array nums and an integer k,
	return the k most frequent elements. You may
	return the answer in any order.

	Example 1:
	Input: nums = [1,1,1,2,2,3], k = 2
	Output: [1,2]

	Example 2:
	Input: nums = [1], k = 1
	Output: [1]


	Constraints:

	1 <= nums.length <= 105
	k is in the range [1, the number of unique
	elements in the array].
	It is guaranteed that the answer is unique.


	Follow up: Your algorithm's time complexity
	must be better than O(n log n), where n is the
	array's size.
*/

package main

import "fmt"


// func topKFrequent(nums []int, k int) []int {
//     // Count
//     freq := map[int]int{}       // S: O(n)

//     for _, n := range nums {    // T: O(n)
//         freq[n]++
//     }

//     // Generating Min heap O(n log k)
//     minHeap := &IntHeap{}
//     for key, val := range freq {            // T: O(n)
//         heap.Push(minHeap, []int{key, val}) // T: O(log k)
//         if minHeap.Len() > k {
//             heap.Pop(minHeap)               // T: O(log k)
//         }
//     }

//     // Pop T: O(k log k)
//     res := []int{}
//     for range k {// T: O(k)
//         res = append(res, heap.Pop(minHeap).([]int)[0])// T: O(log k) 
//     }

//     return res
// }

// // IntHeap is a min-heap of []ints.
// type IntHeap [][]int

// func (h IntHeap) Len() int           { return len(h) }
// func (h IntHeap) Less(i, j int) bool { return h[i][1] < h[j][1] }
// func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// func (h *IntHeap) Push(x interface{}) {
//     *h = append(*h, x.([]int))
// }

// func (h *IntHeap) Pop() interface{} {
//     old := *h
//     n := len(old)
//     x := old[n-1]
//     *h = old[0 : n-1]
//     return x
// }



func topKFrequent(nums []int, k int) []int {
    freq := map[int]int{}     // S: O(n)

    for _, n := range nums {    // T: O(n)
        freq[n]++
    }

    freqBuckets := make([][]int, len(nums)+1)  // S: O(n)
    for key, val := range freq {      // T: O(n)
        freqBuckets[val] = append(freqBuckets[val], key)
    }

    topK := []int{} // S: O(K)
    for i := len(freqBuckets)-1; i > -1; i-- { // T O(n) [outer] + O(n) [total inner work, summed] = O(n)
        for _, n := range freqBuckets[i] {
            if len(topK) == k {
                return topK
            }
            topK = append(topK, n)
        }
    }

    return topK
}


func main() {
	fmt.Println([]int{1, 1, 1, 2, 2, 3}, 2)
}

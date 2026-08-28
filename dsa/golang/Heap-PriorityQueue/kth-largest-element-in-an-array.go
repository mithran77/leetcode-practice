/*

    215. Kth Largest Element in an Array

    Given an integer array nums and an integer k,
    return the kth largest element in the array.

    Note that it is the kth largest element in the
    sorted order, not the kth distinct element.

    Can you solve it without sorting?

    Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

    Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104

*/

// QuickSelect

func findKthLargest(nums []int, k int) int {
    k = len(nums) - k

    var quickSelect func(l, r int) int
    quickSelect = func(l, r int) int {
        pivot, pIdx := nums[r], l

        for i := l; i < r; i++ {
            if nums[i] <= pivot {
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx++
            }
        }

        nums[pIdx], nums[r] = nums[r], nums[pIdx]

        if k < pIdx {
            return quickSelect(l, pIdx - 1)
        } else if k > pIdx {
            return quickSelect(pIdx + 1, r)
        } else {
            return nums[pIdx]
        }

    }

    return quickSelect(0, len(nums) - 1)
}




import "container/heap"

func findKthLargest(nums []int, k int) int {
    maxHeap := &IntHeap{}
    *maxHeap = append(*maxHeap, nums...)
    heap.Init(maxHeap)

    res := 0
    for range k {
        res = heap.Pop(maxHeap).(int)
    }
    return res
}


// IntHeap is a max-heap of int.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}



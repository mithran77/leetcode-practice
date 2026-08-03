/*

    295. Find Median from Data Stream

    The median is the middle value in an ordered integer
    list. If the size of the list is even, there is no
    middle value, and the median is the mean of the two
    middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3],
    the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the
    data stream to the data structure.
    double findMedian() returns the median of all elements
    so far. Answers within 10-5 of the actual answer will
    be accepted.

    Example 1:
    Input
    ["MedianFinder", "addNum", "addNum", "findMedian",
    "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
    Output
    [null, null, null, 1.5, null, 2.0]

    Explanation
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0

    Constraints:
    -105 <= num <= 105
    There will be at least one element in the data structure
    before calling findMedian. At most 5 * 104 calls will
    be made to addNum and findMedian.

    Follow up:
    If all integer numbers from the stream are in the range
    [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the
    range [0, 100], how would you optimize your solution?

*/


type MedianFinder struct {
    minHeap *MinHeap
    maxHeap *MaxHeap
}


func Constructor() MedianFinder {
    mf := MedianFinder{
        minHeap: &MinHeap{},
        maxHeap: &MaxHeap{},
    }

    return mf
}


func (mf *MedianFinder) AddNum(num int)  {
    if mf.maxHeap.Len() > 0 && num <= (*mf.maxHeap)[0] {
        heap.Push(mf.maxHeap, num)
    } else {
        heap.Push(mf.minHeap, num)
    }

    // Balance
    if mf.minHeap.Len() > (mf.maxHeap.Len() + 1) {
        n := heap.Pop(mf.minHeap).(int)
        heap.Push(mf.maxHeap, n)
    } else if mf.maxHeap.Len() > (mf.minHeap.Len() + 1) {
        n := heap.Pop(mf.maxHeap).(int)
        heap.Push(mf.minHeap, n)
    }
}


func (mf *MedianFinder) FindMedian() float64 {
    if mf.maxHeap.Len() > mf.minHeap.Len()  {
        return float64((*mf.maxHeap)[0])
    } else if mf.minHeap.Len() > mf.maxHeap.Len() {
        return float64((*mf.minHeap)[0])
    } else {
        mn := float64((*mf.minHeap)[0])
        mx := float64((*mf.maxHeap)[0])
        return (mn + mx) / 2
    }

}


/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */


// MaxHeap is a max-heap of int.

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}


// MinHeap is a min-heap of int.

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

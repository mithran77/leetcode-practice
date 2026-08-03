/*

    973. K Closest Points to Origin

    Given an array of points where points[i] = [xi, yi]
    represents a point on the X-Y plane and an integer k,
    return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is
    the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer
    is guaranteed to be unique (except for the order
    that it is in).

    Example 1:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest k = 1 points from the origin,
    so the answer is just [[-2,2]].

    Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be
    accepted.

    Constraints:

    1 <= k <= points.length <= 104
    -104 <= xi, yi <= 104

*/

// MinHeap

import "container/heap"

type point struct {
    dist int
    coord []int
}

func kClosest(points [][]int, k int) [][]int {
    minHeap := &IntHeap{}
    heap.Init(minHeap)
    for _, p := range points {
        coord := []int{p[0], p[1]}
        d := p[0]*p[0] + p[1]*p[1]
        heap.Push(minHeap, &point{dist: d, coord: coord})
    }

    res := [][]int{}
    for range k {
        res = append(res, heap.Pop(minHeap).(*point).coord)
    }

    return res
}


// IntHeap is a min-heap of ints.
type IntHeap []*point

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].dist < h[j].dist }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(*point))
}

func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

// MaxHeap


import "container/heap"

type point struct {
    dist int
    coord []int
}

func kClosest(points [][]int, k int) [][]int {
    maxHeap := &IntHeap{}

    heap.Init(maxHeap)
    for _, p := range points {
        coord := []int{p[0], p[1]}
        d := p[0]*p[0] + p[1]*p[1]
        heap.Push(maxHeap, &point{dist: d, coord: coord})
        if maxHeap.Len() > k {
            heap.Pop(maxHeap)
        }
    }

    res := [][]int{}
    for range k {
        res = append(res, heap.Pop(maxHeap).(*point).coord)
    }

    return res
}


// IntHeap is a max-heap of points.
type IntHeap []*point

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].dist > h[j].dist }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(*point))
}

func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

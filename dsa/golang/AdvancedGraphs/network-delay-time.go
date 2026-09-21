/*

    743. Network Delay Time

    You are given a network of n nodes, labeled
    from 1 to n. You are also given times,
    a list of travel times as directed edges
    times[i] = (ui, vi, wi), where ui is the
    source node, vi is the target node,
    and wi is the time it takes for a signal to
    travel from source to target.

    We will send a signal from a given node k.
    Return the minimum time it takes for all the
    n nodes to receive the signal. If it is
    impossible for all the n nodes to receive
    the signal, return -1.

    Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]],
    n = 4, k = 2
    Output: 2

    Example 2:
    Input: times = [[1,2,1]], n = 2, k = 1
    Output: 1

    Example 3:
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1

    Constraints:
    1 <= k <= n <= 100
    1 <= times.length <= 6000
    times[i].length == 3
    1 <= ui, vi <= n
    ui != vi
    0 <= wi <= 100
    All the pairs (ui, vi) are unique.
    (i.e., no multiple edges.)

*/

// Dijkstra's
func networkDelayTime(times [][]int, n int, k int) int {
    mh := &MinHeap{}
    heap.Push(mh, []int{0, k - 1})

    adj := map[int][][]int{}
    for i := range n { adj[i] = [][]int{} }
    for _, t := range times {
        u, v, w := t[0], t[1], t[2]
        adj[u - 1] = append(adj[u - 1], []int{w, v - 1})
    }

    minDist := slices.Repeat([]int{-1}, n)
    minTime := -1
    for mh.Len() > 0 {
        pair := heap.Pop(mh).([]int)
        w, v := pair[0], pair[1]
        if minDist[v] != -1 {
            continue
        }
        minTime = max(minTime, w)
        minDist[v] = w

        for _, nei := range adj[v] {
            nw, nv := nei[0], nei[1]
            if minDist[nv] == -1 {
                heap.Push(mh, []int{w + nw, nv})
            }
        }
    }

    for _, n := range minDist {
        if n == -1 {
            return -1
        }
    }
    return minTime
}

type MinHeap [][]int
func (mh MinHeap) Len() int { return len(mh) }
func (mh MinHeap) Less(i, j int) bool { return mh[i][0] < mh[j][0] }
func (mh MinHeap) Swap(i, j int) { mh[i], mh[j] = mh[j], mh[i] }
func (mh *MinHeap) Push(x interface{}) {
    *mh = append(*mh, x.([]int))
}
func (mh *MinHeap) Pop() interface{} {
    x := (*mh)[len(*mh)-1]
    *mh = (*mh)[:len(*mh)-1]
    return x
}



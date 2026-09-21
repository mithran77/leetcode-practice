/*

    1851. Minimum Interval to Include Each Query

    You are given a 2D integer array intervals,
    where intervals[i] = [lefti, righti]
    describes the ith interval starting at lefti
    and ending at righti (inclusive). The size
    of an interval is defined as the number of
    integers it contains, or more formally
    righti - lefti + 1.

    You are also given an integer array queries.
    The answer to the jth query is the size of the
    smallest interval i such that
    lefti <= queries[j] <= righti.
    If no such interval exists, the answer is -1.

    Return an array containing the answers to the
    queries.

    Example 1:
    Input: intervals = [[1,4],[2,4],[3,6],[4,4]],
    queries = [2,3,4,5]
    Output: [3,3,1,4]
    Explanation: The queries are processed as follows:
    - Query = 2: The interval [2,4] is the
    smallest interval containing 2.
    The answer is 4 - 2 + 1 = 3.
    - Query = 3: The interval [2,4] is the
    smallest interval containing 3.
    The answer is 4 - 2 + 1 = 3.
    - Query = 4: The interval [4,4] is the
    smallest interval containing 4.
    The answer is 4 - 4 + 1 = 1.
    - Query = 5: The interval [3,6] is the
    smallest interval containing 5.
    The answer is 6 - 3 + 1 = 4.

    Example 2:
    Input: intervals = [[2,3],[2,5],[1,8],[20,25]],
    queries = [2,19,5,22]
    Output: [2,-1,4,6]
    Explanation: The queries are processed as follows:
    - Query = 2: The interval [2,3] is the
    smallest interval containing 2.
    The answer is 3 - 2 + 1 = 2.
    - Query = 19: None of the intervals contain 19.
    The answer is -1.
    - Query = 5: The interval [2,5] is the
    smallest interval containing 5.
    The answer is 5 - 2 + 1 = 4.
    - Query = 22: The interval [20,25] is the
    smallest interval containing 22.
    The answer is 25 - 20 + 1 = 6.

    Constraints:
    1 <= intervals.length <= 105
    1 <= queries.length <= 105
    intervals[i].length == 2
    1 <= lefti <= righti <= 107
    1 <= queries[j] <= 107

*/

func minInterval(intervals [][]int, queries []int) []int {
    // Create query map of indexes {q: idx}
    qMap := map[int][]int{}
    for i, q := range queries {
        qMap[q] = append(qMap[q], i)
    }

    // Sort by start times
    slices.SortStableFunc(intervals, func(a, b []int) int {
        return cmp.Compare(a[0], b[0])
    })

    // Create minHeap {len, start, end}
    mh := &MinHeap{}
    res := make([]int, len(queries))
    i := 0

    for _, q := range slices.Sorted(maps.Keys(qMap)) {

        // Push all valid intervals by start 
        for i < len(intervals) && intervals[i][0] <= q {
            start, end := intervals[i][0], intervals[i][1]
            heap.Push(mh, []int{end - start + 1, start, end})
            i++
        }

        // Discard invalid intervals by end
        for mh.Len() > 0 && (*mh)[0][2] < q {
            heap.Pop(mh)
        }

        for _, idx := range qMap[q] {
            if mh.Len() == 0 {
                res[idx] = -1
            } else {
                res[idx] = (*mh)[0][0]
            }
        }

    }

    return res
}

type MinHeap [][]int

func (mh MinHeap) Len() int { return len(mh) }
func (mh MinHeap) Less(a, b int) bool { return mh[a][0] < mh[b][0] }
func (mh MinHeap) Swap(a, b int) { mh[a], mh[b] = mh[b], mh[a] }
func (mh *MinHeap) Push(x interface{}) {
    *mh = append(*mh, x.([]int))
}
func (mh *MinHeap) Pop() interface{} {
    x := (*mh)[len(*mh)-1]
    *mh = (*mh)[:len(*mh)-1]
    return x
}


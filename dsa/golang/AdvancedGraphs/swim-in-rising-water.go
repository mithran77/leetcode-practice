/*
    778. Swim in Rising Water

    You are given an n x n integer matrix
    grid where each value grid[i][j]
    represents the elevation at that point (i, j).

    The rain starts to fall. At time t, the
    depth of the water everywhere is t.
    You can swim from a square to another
    4-directionally adjacent square if and
    only if the elevation of both squares
    individually are at most t. You can swim
    infinite distances in zero time.
    Of course, you must stay within the
    boundaries of the grid during your swim.

    Return the least time until you can reach the
    bottom right square (n - 1, n - 1) if you start
    at the top left square (0, 0).

    Example 1:
    Input: grid = [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because
    4-directionally adjacent neighbors have a
    higher elevation than t = 0.
    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim
    anywhere inside the grid.

    Example 2:
    Input: grid = [[0,1,2,3,4],[24,23,22,21,5],
    [12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation: The final route is shown.
    We need to wait until time 16 so that (0, 0)
    and (4, 4) are connected.


    Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 50
    0 <= grid[i][j] < n2
    Each value grid[i][j] is unique.
*/

// Djikstra's
func swimInWater(grid [][]int) int {
    gLen := len(grid)

    mh := &MinHeap{}
    heap.Push(mh, []int{grid[0][0], 0, 0})

    nei := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    visit := make([][]bool, gLen)
    for i := range gLen { visit[i] = make([]bool, gLen) }

    for mh.Len() > 0 {
        v := heap.Pop(mh).([]int)
        h, r, c:= v[0], v[1], v[2]
        if r ==  gLen -1 && c == gLen - 1 {
            return h
        }

        for _, n := range nei {
            nr, nc := r + n[0], c + n[1]
            if ((0 <= nr && nr < gLen) &&
                (0 <= nc && nc < gLen) &&
                (!visit[nr][nc])) {
                    nh := max(h, grid[nr][nc])
                    heap.Push(mh, []int{nh, nr, nc})
                    visit[nr][nc] = true
                }
        }
    }
    return -1
}

type MinHeap [][]int
func (mh MinHeap) Len() int { return len(mh) }
func (mh MinHeap) Less(i, j int) bool { return mh[i][0] < mh[j][0] }
func (mh MinHeap) Swap(i, j int) { mh[i], mh[j] = mh[j], mh[i] }
func (mh *MinHeap) Push(x interface{}) {
    *mh = append(*mh, x.([]int))
}
func (mh *MinHeap) Pop() interface{} {
    x := (*mh)[len(*mh) - 1]
    *mh = (*mh)[:len(*mh) - 1]
    return x
}

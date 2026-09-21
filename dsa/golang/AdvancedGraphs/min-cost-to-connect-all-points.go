/*

    1584. Min Cost to Connect All Points

    You are given an array points representing
    integer coordinates of some points on a
    2D-plane, where points[i] = [xi, yi].

    The cost of connecting two points [xi, yi]
    and [xj, yj] is the manhattan distance
    between them: |xi - xj| + |yi - yj|,
    where |val| denotes the absolute value of val.

    Return the minimum cost to make all points
    connected. All points are connected if there
    is exactly one simple path between any two points.

    Example 1:
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
    Explanation: 
    We can connect the points as shown above to
    get the minimum cost of 20. Notice that there is
    a unique path between every pair of points.

    Example 2:
    Input: points = [[3,12],[-2,5],[-4,1]]
    Output: 18

    Constraints:
    1 <= points.length <= 1000
    -106 <= xi, yi <= 106
    All pairs (xi, yi) are distinct.

*/

// Kruskal
func minCostConnectPoints(points [][]int) int {
    dsu := createDSU(len(points))
    mh := &MinHeap{}

    for i := 0; i < len(points); i++ {
        for j := i+1; j < len(points); j++ {
            x1,  y1 := points[i][0], points[i][1]
            x2,  y2 := points[j][0], points[j][1]
            md := abs(x1 - x2) + abs(y1 - y2)
            heap.Push(mh, []int{md, i, j})
        }
    }

    mstSum := 0
    for mh.Len() > 0 {
        edge := heap.Pop(mh).([]int)
        md, coord1, coord2 := edge[0], edge[1], edge[2]
        if dsu.union(coord1, coord2) {
            mstSum += md
        }
    }

    return mstSum
}

type DSU struct {
    parent []int
    cost []int
}

func createDSU(n int) DSU {
    parent := make([]int, n)
    for i := range n { parent[i] = i }
    d := DSU {
        parent: parent,
        cost: slices.Repeat([]int{0}, n),
    }
    return d
}

func (d *DSU) find(n int) int {
    if d.parent[n] != n {
        d.parent[n] = d.find(d.parent[n])
    }
    return d.parent[n]
}

func (d *DSU) union(u, v int) bool {
    pu, pv := d.find(u), d.find(v)
    if pu == pv {
        return false
    }

    if d.cost[pu] > d.cost[pv] {
        d.parent[pv] = pu
        d.cost[pu] += d.cost[pv]
    } else {
        d.parent[pu] = pv
        d.cost[pv] += d.cost[pu]
    }
    return true
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

func abs(x int) int {
    if x >= 0 {
        return x
    }
    return -x
}

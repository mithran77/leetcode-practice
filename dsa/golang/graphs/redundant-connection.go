/*

    684. Redundant Connection

    In this problem, a tree is an undirected
    graph that is connected and has no cycles.

    You are given a graph that started as a
    tree with n nodes labeled from 1 to n, with
    one additional edge added. The added edge has
    two different vertices chosen from 1 to n, and
    was not an edge that already existed.
    The graph is represented as an array edges of
    length n where edges[i] = [ai, bi] indicates
    that there is an edge between nodes ai and bi
    in the graph.

    Return an edge that can be removed so that the
    resulting graph is a tree of n nodes. If there
    are multiple answers, return the answer that
    occurs last in the input.

    Example 1:
    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]

    Example 2:
    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]

    Constraints:
    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    There are no repeated edges.
    The given graph is connected.
    
*/

func findRedundantConnection(edges [][]int) []int {
    d := create(len(edges))

    for _, e := range edges {
        if d.find(e[0]) == d.find(e[1]) {
            return []int{e[0], e[1]}
        }
        d.union(e[0], e[1])
    }
    return []int{}
}

type DSU struct {
    parent []int
    size []int
}

func create(n int) *DSU {
    parent := make([]int, n + 1)
    for i := range (n + 1) {
        parent[i] = i
    }
    return &DSU{
        parent: parent,
        size: make([]int, n + 1),
    }
}

func (d *DSU) find(n int) int {
    if d.parent[n] != n {
        d.parent[n] = d.find(d.parent[n])
    }

    return d.parent[n]
}

func (d *DSU) union(u, v int) {
    pu, pv := d.find(u), d.find(v)

    if pu == pv {
        return
    }
    if d.size[pu] > d.size[pv] {
        d.parent[pv] = pu
        d.size[pu] += d.size[pv]
    } else {
        d.parent[pu] = pv
        d.size[pv] += d.size[pu]
    }

}


/*

    https://neetcode.io/problems/count-connected-components
    Count Connected Components
    There is an undirected graph with n nodes. There is also
    an edges array, where edges[i] = [a, b] means that there
    is an edge between node a and node b in the graph.

    The nodes are numbered from 0 to n - 1.

    Return the total number of connected components in that graph.

    Example 1:
    Input:
    n=3
    edges=[[0,1], [0,2]]
    Output:
    1

    Example 2:
    Input:
    n=6
    edges=[[0,1], [1,2], [2,3], [4,5]]
    Output:
    2

    Constraints:
    1 <= n <= 100
    0 <= edges.length <= n * (n - 1) / 2

*/

// dfs

// func countComponents(n int, edges [][]int) int {

// 	adj := map[int][]int{}
// 	for _, e := range edges {
// 		adj[e[0]] = append(adj[e[0]], e[1])
// 		adj[e[1]] = append(adj[e[1]], e[0])
// 	}

// 	visit := map[int]struct{}{}
// 	var dfs func(node int)
// 	dfs = func(node int) {
// 		if _, exists := visit[node]; exists {
// 			return
// 		}

// 		visit[node] = struct{}{}
// 		for _, nei := range adj[node] {
// 			dfs(nei)
// 		}
// 	}

//     components := 0
// 	for i := range n {
// 		if _, exists := visit[i]; !exists {
// 			dfs(i)
// 			components++
// 		}
// 	}

// 	return components
// }


func countComponents(n int, edges [][]int) int {
    d := create(n)
	for _, e := range edges {
		u, v := e[0], e[1]
		d.union(u, v)
	}

	components := 0
	for i := range d.parent {
		if d.find(i) == i {
			components++
		}
	}

	return components
}


type DSU struct {
	parent []int
	rank []int
}

func create(n int) *DSU {
	parent := make([]int, n)
	for i := range n {
		parent[i] = i
	}

	return &DSU{
		parent: parent,
		rank: make([]int, n),
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

	if d.rank[pu] > d.rank[pv] {
		d.parent[pv] = pu
	} else if d.rank[pv] > d.rank[pu] {
		d.parent[pu] = pv
	} else {
		d.parent[pu] = pv
		d.rank[pv]++
	}
}


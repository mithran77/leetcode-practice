/*
    Valid Tree
    https://neetcode.io/problems/valid-tree

    Given n nodes labeled from 0 to n - 1 and a list
    of undirected edges (each edge is a pair of nodes), 
    write a function to check whether these edges
    make up a valid tree.

    Example 1:

    Input:
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

    Output:
    true
    Example 2:

    Input:
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

    Output:
    false
    Note:

    You can assume that no duplicate edges will appear
    in edges. Since all edges are undirected, [0, 1] is
    the same as [1, 0] and thus will not appear together
    in edges.

    Constraints:

    1 <= n <= 100
    0 <= edges.length <= n * (n - 1) / 2
*/

// func validTree(n int, edges [][]int) bool {
//     visit := map[int]bool{}
// 	adj := make([][]int, n)
// 	for _, e := range edges {
// 		adj[e[0]] = append(adj[e[0]], e[1])
// 		adj[e[1]] = append(adj[e[1]], e[0])
// 	}

// 	var dfs func(node, parent int) bool
// 	dfs = func(node, parent int) bool {
// 		if _, exists := visit[node]; exists {
// 			return false
// 		}
// 		visit[node] = true
// 		for _, nei := range adj[node] {
// 			if nei == parent {
// 				continue
// 			}
// 			if !dfs(nei, node) {
// 				return false
// 			}
// 		}
// 		return true
// 	}

// 	if dfs(0, -1) {
// 		return len(visit) == n
// 	} else {
// 		return false
// 	}

// }

func validTree(n int, edges [][]int) bool {
	if len(edges) != n - 1 {
		return false
	}

    d := create(n)
	for _, e := range edges {
		if d.find(e[0]) == d.find(e[1]) {
			return false
		}
		d.union(e[0], e[1])
	}

	components := 0
	for i := range n {
		if d.find(i) == i {
			components++
		}
	}

	return components == 1
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


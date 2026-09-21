/*

    787. Cheapest Flights Within K Stops

    There are n cities connected by some
    number of flights. You are given an array
    flights where flights[i] = [fromi, toi, pricei]
    indicates that there is a flight from
    city fromi to city toi with cost pricei.

    You are also given three integers src,
    dst, and k, return the cheapest price from
    src to dst with at most k stops.
    If there is no such route, return -1.

    Example 1:
    Input: n = 4, flights = [[0,1,100],[1,2,100],
    [2,0,100],[1,3,600],[2,3,200]], src = 0,
    dst = 3, k = 1
    Output: 700
    Explanation:
    The graph is shown above.
    The optimal path with at most 1 stop from
    city 0 to 3 is marked in red and has cost
    100 + 600 = 700.
    Note that the path through cities [0,1,2,3]
    is cheaper but is invalid because it uses 2 stops.

    Example 2:
    Input: n = 3, flights = [[0,1,100],[1,2,100],
    [0,2,500]], src = 0, dst = 2, k = 1
    Output: 200
    Explanation:
    The graph is shown above.
    The optimal path with at most 1 stop from
    city 0 to 2 is marked in red and has cost
    100 + 100 = 200.

    Example 3:
    Input: n = 3, flights = [[0,1,100],[1,2,100],
    [0,2,500]], src = 0, dst = 2, k = 0
    Output: 500
    Explanation:
    The graph is shown above.
    The optimal path with no stops from city 0
    to 2 is marked in red and has cost 500.

    Constraints:
    1 <= n <= 100
    0 <= flights.length <= (n * (n - 1) / 2)
    flights[i].length == 3
    0 <= fromi, toi < n
    fromi != toi
    1 <= pricei <= 104
    There will not be any multiple flights between
    two cities.
    0 <= src, dst, k < n
    src != dst

*/

//BFS
func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
    queue := [][]int{{src, 0}}
    adj := map[int][][]int{}
    for i := range n { adj[i] = [][]int{} }
    for _, f := range flights {
        u, v, w := f[0], f[1], f[2]
        adj[u] = append(adj[u], []int{v, w})
    }

    stops := 0
    cheapestPrice := slices.Repeat([]int{math.MaxInt}, n)
    cheapestPrice[src] = 0

    for len(queue) > 0 && stops <= k {
        qLen := len(queue)
        for range qLen {
            ticket := queue[0]
            queue = queue[1:]
            v, w := ticket[0], ticket[1]

            for _, nei := range adj[v] {
                nv, nw := nei[0], nei[1]
                newPrice := w + nw
                if newPrice < cheapestPrice[nv] {
                    cheapestPrice[nv] = newPrice
                    queue = append(queue, []int{nv, newPrice})
                }
            }
        }
        stops++
    }

    if cheapestPrice[dst] == math.MaxInt {
        return -1
    }

    return cheapestPrice[dst]
}
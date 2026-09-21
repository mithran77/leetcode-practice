/*

    332. Reconstruct Itinerary

    You are given a list of airline tickets
    where tickets[i] = [fromi, toi] represent
    the departure and the arrival airports
    of one flight. Reconstruct the itinerary
    in order and return it.

    All of the tickets belong to a man who
    departs from "JFK", thus, the itinerary
    must begin with "JFK". If there are
    multiple valid itineraries, you should
    return the itinerary that has the smallest
    lexical order when read as a single string.

    For example, the itinerary ["JFK", "LGA"]
    has a smaller lexical order than
    ["JFK", "LGB"]. You may assume all tickets
    form at least one valid itinerary. You
    must use all the tickets once and only once.

    Example 1:
    Input: tickets = [["MUC","LHR"],["JFK","MUC"],
    ["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]

    Example 2:
    Input: tickets = [["JFK","SFO"],["JFK","ATL"],
    ["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is
    ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is
    larger in lexical order.

    Constraints:
    1 <= tickets.length <= 300
    tickets[i].length == 2
    fromi.length == 3
    toi.length == 3
    fromi and toi consist of uppercase English letters.
    fromi != toi

*/

// DFS
func findItinerary(tickets [][]string) []string {
    adj := map[string]*MinHeap{}
    for _, tkt := range tickets {
        if _, exists := adj[tkt[0]]; !exists {
            adj[tkt[0]] = &MinHeap{}
        }
        heap.Push(adj[tkt[0]], tkt[1])
    }

    itinerary := []string{}
    var dfs func(airport string)
    dfs = func(airport string) {
        for adj[airport] != nil && adj[airport].Len() > 0 {
            dest := heap.Pop(adj[airport]).(string)
            dfs(dest)
        }
        itinerary = append(itinerary, airport)
    }
    dfs("JFK")

    slices.Reverse(itinerary)
    return itinerary
}

type MinHeap []string

func (mh MinHeap) Len() int { return len(mh) }
func (mh MinHeap) Less(i, j int) bool { return mh[i] < mh[j] }
func (mh MinHeap) Swap(i, j int) { mh[i], mh[j] = mh[j], mh[i] }
func (mh *MinHeap) Push(x interface{}) {
    *mh = append(*mh, x.(string))
}
func (mh *MinHeap) Pop() interface{} {
    x := (*mh)[len(*mh) - 1]
    *mh = (*mh)[:len(*mh) - 1]
    return x
}

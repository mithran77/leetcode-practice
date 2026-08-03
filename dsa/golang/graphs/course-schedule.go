/*
    207. Course Schedule

    There are a total of numCourses courses you have to
    take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where
    prerequisites[i] = [ai, bi] indicates that you must 
    take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to
    take course 0 you have to first take course 1.
    Return true if you can finish all courses.
    Otherwise, return false.

    Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0.
    So it is possible.

    Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0,
    and to take course 0 you should also have 
    finished course 1. So it is impossible.

    Constraints:

    1 <= numCourses <= 105
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
*/

func canFinish(numCourses int, prerequisites [][]int) bool {
    // Create adjacency & inDegrees
    adj := make([][]int, numCourses)
    inDegrees := make([]int, numCourses)
    for _, p := range prerequisites {
        adj[p[0]] = append(adj[p[0]], p[1])
        inDegrees[p[1]]++
    }

    q := []int{}
    complete := 0
    for n := range inDegrees {
        if inDegrees[n] == 0 {
            complete++
            q = append(q, n)
        }
    }

    // topoSort := []int{}
    
    for len(q) > 0 {
        n := q[0]
        q = q[1:]

        for _, nei := range adj[n] {
            inDegrees[nei]--
            if inDegrees[nei] == 0 {
                complete++
                q = append(q, nei)
            }
        }
        // topoSort = append(topoSort, n)
    }

    // // Reverse in-place
    // tLen := len(topoSort)
    // for i := range (tLen/2) {
    //     topoSort[i], topoSort[tLen-i] = topoSort[tLen-i], topoSort[i]
    // }

    return complete == numCourses
}

/*

    621. Task Scheduler

    You are given an array of CPU tasks, each labeled
    with a letter from A to Z, and a number n.
    Each CPU interval can be idle or allow the
    completion of one task. Tasks can be completed in any order,
    but there's a constraint: there has to be a gap
    of at least n intervals between two tasks with the same label.

    Return the minimum number of CPU intervals required
    to complete all tasks.

    Example 1:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A possible sequence is: A -> B -> idle
    -> A -> B -> idle -> A -> B.
    After completing task A, you must wait two intervals
    before doing A again. The same applies to task B. In
    the 3rd interval, neither A nor B can be done, so you idle.
    By the 4th interval, you can do A again as 2 intervals have passed.

    Example 2:
    Input: tasks = ["A","C","A","B","D","B"], n = 1
    Output: 6
    Explanation: A possible sequence is: A -> B -> C -> D ->
    A -> B.
    With a cooling interval of 1, you can repeat a task after
    just one other task.

    Example 3:
    Input: tasks = ["A","A","A", "B","B","B"], n = 3
    Output: 10
    Explanation: A possible sequence is: A -> B -> idle -> idle
    -> A -> B -> idle -> idle -> A -> B.
    There are only two types of tasks, A and B, which need to be
    separated by 3 intervals. This leads to idling twice between
    repetitions of these tasks.

    Constraints:
    1 <= tasks.length <= 104
    tasks[i] is an uppercase English letter.
    0 <= n <= 100

*/


import "container/heap"

func leastInterval(tasks []byte, n int) int {
    tCount := map[byte]int{}
    for _, t := range tasks {
        tCount[t]++
    }

    freeQ := &IntHeap{}
    for _, v := range tCount {
        *freeQ = append(*freeQ, v)
    }
    heap.Init(freeQ)

    idleQ := [][]int{}
    tick := 0

    for freeQ.Len() > 0 || len(idleQ) > 0 {
        tick++

        if freeQ.Len() > 0 {
            remain := heap.Pop(freeQ).(int)
            if remain--; remain > 0 {
                idleQ = append(idleQ, []int{remain, tick + n})
            }
        }

        if len(idleQ) > 0 && idleQ[0][1] == tick {
            task := idleQ[0]
            idleQ = idleQ[1:]
            heap.Push(freeQ, task[0])
        }
    }

    return tick
}

// IntHeap is a max-heap of int.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

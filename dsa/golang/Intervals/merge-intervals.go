/*

    56. Merge Intervals

    Given an array of intervals where
    intervals[i] = [starti, endi], merge
    all overlapping intervals, and return
    an array of the non-overlapping
    intervals that cover all the intervals
    in the input.

    Example 1:
    Input: intervals = [[1,3],[2,6],
    [8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3]
    and [2,6]
    overlaps, merge them into [1,6].

    Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and
    [4,5] are
    considered overlapping.

    Constraints:
    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

*/

// Line Sweep
func merge(intervals [][]int) [][]int {

    times := [][]int{}
	for _, i := range intervals {
		times = append(times, []int{i[0], 1})
		times = append(times, []int{i[1], -1})
	}

	slices.SortStableFunc(times, func(a, b []int) int {
		if (a[0] == b[0]) {
			return cmp.Compare(b[1], a[1])
		}
		return cmp.Compare(a[0], b[0])
	})

	overlap := 0
    interval, res := []int{}, [][]int{}
	for _, t := range times {
        if len(interval) == 0 {
            interval = append(interval, t[0])
        }

		overlap += t[1]

        if overlap == 0 {
            interval = append(interval, t[0])          
            res = append(res, interval)
            interval = []int{}
        }

	}

	return res

}

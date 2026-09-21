/*

    57. Insert Interval

    You are given an array of
    non-overlapping intervals intervals
    where intervals[i] = [starti, endi]
    represent the start and the end of
    the ith interval and intervals is
    sorted in ascending order by starti.
    You are also given an interval
    newInterval = [start, end]
    that represents the start and end
    of another interval.

    Insert newInterval into intervals such
    that intervals is still sorted in
    ascending order by start and intervals
    still does not have any overlapping
    intervals (merge overlapping intervals
    if necessary).

    Return intervals after the insertion.

    Note that you don't need to modify
    intervals in-place. You can make a new
    array and return it.

    Example 1:
    Input: intervals = [[1,3],[6,9]],
    newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],
    [8,10],[12,16]],
    newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval
    [4,8] overlaps with [3,5],[6,7],[8,10].

    Constraints:
    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending
    order.
    newInterval.length == 2
    0 <= start <= end <= 105

*/

func insert(intervals [][]int, newInterval []int) [][]int {
    intervals = append(intervals, newInterval)

    times := [][]int{}
	for _, iv := range intervals {
		times = append(times, []int{iv[0], 1})
		times = append(times, []int{iv[1], -1})
	}

	slices.SortStableFunc(times, func(a, b []int) int {
		if a[0] == b[0] {
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

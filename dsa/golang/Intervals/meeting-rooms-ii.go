/*
    Meeting Schedule II
    Given an array of meeting time interval
    objects consisting of start and end times
    [[start_1,end_1],[start_2,end_2],...]
    (start_i < end_i), find the minimum
    number of days required to schedule
    all meetings without any conflicts.

    Example 1:
    Input: intervals = [(0,40),(5,10),
    (15,20)]
    Output: 2
    Explanation:
    day1: (0,40)
    day2: (5,10),(15,20)

    Example 2:
    Input: intervals = [(4,9)]
    Output: 1

    Note:
    (0,8),(8,10) is not considered a
    conflict at 8

    Constraints:
    0 <= intervals.length <= 500
    0 <= intervals[i].start <
    intervals[i].end <= 1,000,000
*/

// 2P
/**
 * Definition of Interval:
 * type Interval struct {
 *    start int
 *    end   int
 * }
 */
import "slices"
func minMeetingRooms(intervals []Interval) int {

	minRooms := 0
	start, end := make([]int, len(intervals)), make([]int, len(intervals))
	for i := 0; i < len(intervals); i++ {
		start[i], end[i] = intervals[i].start, intervals[i].end
	}
	slices.Sort(start); slices.Sort(end)

	s, e := 0, 0
	rooms := 0
	for s < len(intervals) {
		if start[s] < end[e] {
			s++
			rooms++
		} else {
			e++
			rooms--
		}
		minRooms = max(minRooms, rooms)
	}

	return minRooms
}


// Line sweep
/**
 * Definition of Interval:
 * type Interval struct {
 *    start int
 *    end   int
 * }
 */
import "slices"
import "cmp"

func minMeetingRooms(intervals []Interval) int {

	times := [][]int{}
	for _, i := range intervals {
		times = append(times, []int{i.start, 1})
		times = append(times, []int{i.end, -1})
	}

	slices.SortStableFunc(times, func(a, b []int) int {
		if (a[0] == b[0]) {
			return cmp.Compare(a[1], b[1])
		}
		return cmp.Compare(a[0], b[0])
	})

	minRooms, rooms := 0, 0
	for _, t := range times {
		rooms += t[1]
		minRooms = max(minRooms, rooms)
	}

	return minRooms
}


// Map implementation
/**
 * Definition of Interval:
 * type Interval struct {
 *    start int
 *    end   int
 * }
 */
import "slices"
import "maps"

func minMeetingRooms(intervals []Interval) int {

	points := map[int]int{}
	for _, i := range intervals {
		points[i.start] += 1
		points[i.end] -= 1
	}

	minRooms, rooms := 0, 0
	for _, p := range slices.Sorted(maps.Keys(points)) {
		rooms += points[p]
		minRooms = max(minRooms, rooms)
	}

	return minRooms
}


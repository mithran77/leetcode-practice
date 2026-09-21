/*
    Meeting Schedule

    Given an array of meeting time
    interval objects consisting of
    start and end times [[start_1,end_1],
    [start_2,end_2],...] (start_i < end_i),
    determine if a person could add all
    meetings to their schedule without any
    conflicts.

    Example 1:
    Input: intervals = [(0,30),(5,10),
    (15,20)]
    Output: false
    Explanation:
    (0,30) and (5,10) will conflict
    (0,30) and (15,20) will conflict

    Example 2:
    Input: intervals = [(5,8),(9,15)]
    Output: true

    Note:
    (0,8),(8,10) is not considered a conflict at 8

    Constraints:
    0 <= intervals.length <= 500
    0 <= intervals[i].start
    < intervals[i].end <= 1,000,000
*/

/**
 * Definition of Interval:
 * type Interval struct {
 *    start int
 *    end   int
 * }
 */
import "slices"
import "cmp"

func canAttendMeetings(intervals []Interval) bool {
	slices.SortStableFunc(intervals, func(a, b Interval) int {
		return cmp.Compare(a.start, b.start)
	})

	for i := 1; i < len(intervals); i++ {
		if intervals[i-1].end > intervals[i].start {
			return false
		}
	}

	return true
}


// Line Sweep
// Slice implementation
/**
 * Definition of Interval:
 * type Interval struct {
 *    start int
 *    end   int
 * }
 */
import "slices"
import "cmp"

func canAttendMeetings(intervals []Interval) bool {

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

	rooms := 0
	for _, t := range times {
		rooms += t[1]
		if rooms > 1 {
			return false
		}
	}

	return true
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

func canAttendMeetings(intervals []Interval) bool {

	points := map[int]int{}
	for _, i := range intervals {
		points[i.start] += 1
		points[i.end] -= 1
	}

	rooms := 0
	for _, p := range slices.Sorted(maps.Keys(points)) {
		rooms += points[p]
		if rooms > 1 {
			return false
		}
	}

	return true
}


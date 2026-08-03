/*

    84. Largest Rectangle in Histogram

    Given an array of integers heights
    representing the histogram's bar
    height where the width of each bar is 1,
    return the area of the largest
    rectangle in the histogram.

    Example 1:
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The above is a histogram
    where width of each bar is 1.
    The largest rectangle is shown in the
    red area, which has an area = 10 units.

    Example 2:
    Input: heights = [2,4]
    Output: 4

    Constraints:
    1 <= heights.length <= 105
    0 <= heights[i] <= 104

*/

func largestRectangleArea(heights []int) int {
    stack := [][]int{}
    maxRectangle := 0

    for j, h := range heights {
        start := j
        sLen := len(stack)
        for len(stack) > 0 && h < stack[sLen-1][1] {
            i, topH := stack[sLen-1][0], stack[sLen-1][1]
            maxRectangle = max(maxRectangle, topH * (j - i))
            start = i
        }
        stack = append(stack, []int{start, h})
    }

    for _, s:= range stack {
        i, topH := s[0], s[1]
        maxRectangle = max(maxRectangle, topH * (len(heights) - i))
    }

    return maxRectangle
}

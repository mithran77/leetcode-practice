/*
    739. Daily Temperatures

    Given an array of integers temperatures
    represents the daily temperatures,
    return an array answer such that 
    answer[i] is the number of days you have
    to wait after the ith day to get a
    warmer temperature.
    If there is no future day for which this
    is possible, keep answer[i] == 0
    instead.

    Example 1:
    Input: temperatures = [73,74,75,71,69,
    72,76,73]
    Output: [1,1,4,2,1,1,0,0]

    Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

    Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]

    Constraints:
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100
*/

func dailyTemperatures(temperatures []int) []int {
    stack := [][]int{}          // S: O(n)
    res := slices.Repeat([]int{0}, len(temperatures))   // S: O(n)

    for i, t := range temperatures {    // T: O(n)
        for len(stack) > 0 && stack[len(stack)-1][0] < t {  
            prev := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            res[prev[1]] = i - prev[1]
        }

        stack = append(stack, []int{t, i})
    }

    return res

}

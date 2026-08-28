/*

    239. Sliding Window Maximum

    You are given an array of integers nums, there
    is a sliding window of size k which is moving
    from the very left of the array to the very right.
    You can only see the k numbers in the window.
    Each time the sliding window moves right by one
    position.

    Return the max sliding window.

    Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation: 
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7

    Example 2:
    Input: nums = [1], k = 1
    Output: [1]

    Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length

*/

func maxSlidingWindow(nums []int, k int) []int {
    q, output := []int{}, []int{}
    l, r := 0, 0

    for r < len(nums) {
        for len(q) > 0 && nums[q[len(q)-1]] < nums[r] {
            q = q[:len(q)-1]
        }
        q = append(q, r)

        if q[0] < l {
            q = q[1:]
        }

        if r >= k-1 {
            output = append(output, nums[q[0]])
            l++
        }
        r++

    }

    return output
}

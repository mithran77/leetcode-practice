/*

    7. Reverse Integer

    Given a signed 32-bit integer x,
    return x with its digits reversed.
    If reversing x causes the value to
    go outside the signed 32-bit
    integer range [-231, 231 - 1],
    then return 0.

    Assume the environment does not
    allow you to store 64-bit integers
    (signed or unsigned).

    Example 1:
    Input: x = 123
    Output: 321

    Example 2:
    Input: x = -123
    Output: -321

    Example 3:
    Input: x = 120
    Output: 21

    Constraints:
    -231 <= x <= 231 - 1

*/

// Math
func reverse(x int) int {
    minInt, maxInt := math.MinInt32, math.MaxInt32
    reversed := 0

    for x != 0 {
        digit := x % 10
        x = x / 10

        if reversed < (minInt / 10) || (reversed <= (minInt / 10) && digit < (minInt % 10)) {
            return 0
        }

        if reversed > (maxInt / 10) || (reversed >= (maxInt / 10) && digit > (maxInt % 10)) {
            return 0
        }

        reversed = reversed * 10 + digit
    }

    return reversed
}


// Bit Manip
func reverse(x int) int {
    reversed := 0

    for x != 0 {
        reversed = reversed * 10 + x % 10
        x = x / 10
    }

    if reversed < -(1 << 31) || reversed > (1 << 31) - 1{
        return 0
    }

    return reversed
}

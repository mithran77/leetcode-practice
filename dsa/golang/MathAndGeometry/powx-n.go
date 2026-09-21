/*

    50. Pow(x, n)

    Implement pow(x, n), which
    calculates x raised to the
    power n (i.e., xn).

    Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

    Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

    Constraints:
    -100.0 < x < 100.0
    -231 <= n <= 231-1
    n is an integer.
    Either x is not zero or n > 0.
    -104 <= xn <= 104

*/

// TLE
func myPow(x float64, n int) float64 {
    pow := 1.0
    for range abs(n) {
        if n > 0 {
            pow *= x
        } else {
            pow /= x
        }
        
    }

    return pow
}

func abs(n int) int {
    if n < 0 {
        return -1 * n
    }
    return n
}

// T: O(1)
func myPow(x float64, n int) float64 {
    ans := solve(x, abs(n))
    if n > 0 {
        return ans
    }

    return 1 / ans
}

func solve(x float64, n int) float64 {
    if n == 0 {
        return 1
    }
    if n == 1 {
        return x
    }

    if n % 2 == 0 {
        a := solve(x, n / 2)
        return a * a
    } else {
        a := solve(x, n / 2)
        return x * a * a
    }
}

func abs(n int) int {
    if n < 0 {
        return -1 * n
    }
    return n
}

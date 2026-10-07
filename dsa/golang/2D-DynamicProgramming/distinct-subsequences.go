/*

    115. Distinct Subsequences

    Given two strings s and t, return
    the number of distinct subsequences
    of s which equals t.

    The test cases are generated so that
    the answer fits on a 32-bit signed integer.

    Example 1:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
    As shown below, there are 3 ways you can
    generate "rabbit" from s.
    rabbbit
    rabbbit
    rabbbit

    Example 2:
    Input: s = "babgbag", t = "bag"
    Output: 5
    Explanation:
    As shown below, there are 5 ways you can
    generate "bag" from s.
    babgbag
    babgbag
    babgbag
    babgbag
    babgbag

    Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.

*/

func numDistinct(s string, t string) int {
	dp := make([][]int, len(s))
	for r := range len(s) {
		dp[r] = slices.Repeat([]int{-1}, len(t))
	}

	var rNumDistinct func(i, j int) int
	rNumDistinct = func(i, j int) int {
		if j == len(t) {
			return 1
		}
		if i == len(s) {
			return 0
		}

		if dp[i][j] != -1 {
			return dp[i][j]
		}

		if s[i] == t[j] {
			pick := rNumDistinct(i+1, j+1)
			skip := rNumDistinct(i+1, j)
			dp[i][j] = pick + skip
		} else {
			dp[i][j] = rNumDistinct(i+1, j)
		}

		return dp[i][j]
	}

	return rNumDistinct(0, 0)
}




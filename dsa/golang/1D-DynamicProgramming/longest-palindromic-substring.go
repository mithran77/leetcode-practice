/*

    5. Longest Palindromic Substring

    Given a string s, return the longest
    palindromic substring in s.

    Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid
    answer.

    Example 2:
    Input: s = "cbbd"
    Output: "bb"

    Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English
    letters.

*/

// DP
func longestPalindrome(s string) string {

    dp := make([][]int, len(s))
    for i := range len(s) {
        dp[i] = slices.Repeat([]int{-1}, len(s))
    }
    var rPalindrome func(i, j int) int
    rPalindrome = func(i, j int) int {
        if dp[i][j] != -1 {
            return dp[i][j]
        }
        if i >= j {
            return 1
        }

        if s[i] != s[j] {
            dp[i][j] = 0
        } else {
            dp[i][j] = rPalindrome(i+1, j-1)
        }

        return dp[i][j]

    }

    start, end := 0, 0
    for i := range len(s) {
        for j := i; j < len(s); j++ {

            if rPalindrome(i, j) == 1 && (j - i > end - start) {
                start, end = i, j
            }
        }
    }

    return s[start:end + 1]
}

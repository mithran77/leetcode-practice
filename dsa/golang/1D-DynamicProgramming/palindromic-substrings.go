/*

    647. Palindromic Substrings

    Given a string s, return the number
    of palindromic substrings in it.
    A string is a palindrome when it
    reads the same backward as forward.
    A substring is a contiguous sequence
    of characters within the string.

    Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings:
    "a", "b", "c".

    Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings:
    "a", "a", "a", "aa", "aa", "aaa".

    Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.

*/

// DP

func countSubstrings(s string) int {

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

    palindromes := 0
    for i := range len(s) {
        for j := i; j < len(s); j++ {
            if rPalindrome(i, j) == 1 {
                palindromes++
            }
        }
    }

    return palindromes
}
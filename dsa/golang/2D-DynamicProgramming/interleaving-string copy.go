/*

    10. Regular Expression Matching

    Given an input string s and a pattern
    p, implement regular expression
    matching with support for '.' and
    '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the
    preceding element. Return a boolean
    indicating whether the matching
    covers the entire input string
    (not partial).

    Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the
    entire string "aa".

    Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more
    of the preceding element, 'a'.
    Therefore, by repeating 'a' once,
    it becomes "aa".

    Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more
    (*) of any character (.)".

    Constraints:
    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters,
    '.', and '*'.
    It is guaranteed for each appearance of
    the character '*', there will be a previous
    valid character to match.

*/

func isMatch(s string, p string) bool {
    m, n := len(s), len(p)
    dp := map[[2]int]bool{}

    var rIsMatch func(i ,j int) bool
    rIsMatch = func(i ,j int) bool {
        if i == m && j == n {
            return true
        }

        key := [2]int{i, j}
        if val, exists := dp[key]; exists {
            return val
        }

        singleMatch := (i < m && j < n) && (s[i] == p[j] || p[j] == '.')
        dp[key] = false

        // .* case
        if (j + 1) < n && p[j + 1] == '*' {
            // 0 || 1 char
            dp[key] = rIsMatch(i, j + 2) ||
                       (singleMatch && rIsMatch(i + 1, j))
        } else if singleMatch { // [a-z.]{1}
            dp[key] = rIsMatch(i + 1, j + 1)
        }

        return dp[key]
    }

    return rIsMatch(0, 0)
}


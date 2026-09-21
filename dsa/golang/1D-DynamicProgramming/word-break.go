/*

    139. Word Break

    Given a string s and a dictionary of
    strings wordDict, return true if s
    can be segmented into a space-separated
    sequence of one or more dictionary words.

    Note that the same word in the
    dictionary may be reused multiple
    times in the segmentation.

    Example 1:
    Input: s = "leetcode",
    wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because
    "leetcode" can be segmented as
    "leet code".

    Example 2:
    Input: s = "applepenapple",
    wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because
    "applepenapple" can be segmented
    as "apple pen apple".
    Note that you are allowed to reuse
    a dictionary word.

    Example 3:
    Input: s = "catsandog",
    wordDict = ["cats","dog","sand","and","cat"]
    Output: false

    Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.

*/

func wordBreak(s string, wordDict []string) bool {
    dp := slices.Repeat([]int{-1}, len(s) + 1)

    wordSet := map[string]struct{}{}
    for _, w := range wordDict {
        wordSet[w] = struct{}{}
    }

    var rWordBreak func(i int) int
    rWordBreak = func(i int) int {
        if dp[i] != -1 {
            return dp[i]
        }
        if i >= len(s) {
            return 1
        }

        dp[i] = 0
        for j := i; j <= len(s); j++ {
            _, exists := wordSet[s[i:j]]
            if exists {
                dp[i] += rWordBreak(j)
            }
        }

        if dp[i] > 0 { dp[i] = 1 }
        return dp[i]
    }

    return rWordBreak(0) == 1
}
/*

    76. Minimum Window Substring

    Given two strings s and t of lengths m and n respectively, return the
    minimum window substring of s such that every character in
    (including duplicates) is included in the window. If there is no such
    substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.

    Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
    from string t.
    Example 2:

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
    Example 3:

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

    Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

    Follow up: Could you find an algorithm that runs in O(m + n) time?

*/

package main

import "fmt"

func minWindow(s string, t string) string {
	if len(t) > len(s) {
		return ""
	}

    start, end := 0, -1
	tCount, sCount := map[byte]int{}, map[byte]int{}
	for i := 0; i < len(t); i++ {
		tCount[t[i]]++
		sCount[s[i]]++
	}

	if containsCounts(sCount, tCount) {
		return s[:len(t)]
	}

    slow := 0
	for fast := len(t); fast < len(s); fast++ {
        sCount[s[fast]]++
        for containsCounts(sCount, tCount) {
            // Shrink
            if end == -1 || (fast - slow)  < (end - start) {
                start, end =  slow, fast
            }
            sCount[s[slow]]--
            slow++
        }
	}

    if end == -1 {
        return ""
    }
    return s[start:end+1]
}

func containsCounts(b, a map[byte]int) bool {
	matches := 0
	for c, count := range a {
		if b[c] >= count {
			matches++
		}
	}
	return matches == len(a)
}


func main() {
	fmt.Println(minWindow("ADOBECODEBANC", "ABC"))
	fmt.Println(minWindow("a", "a"))
	fmt.Println(minWindow("a", "aa"))
}

/*
    424. Longest Repeating Character Replacement

    You are given a string s and an integer
    k. You can choose any character of
    the string and change it to any other
    uppercase English character. You can perform
    this operation at most k times.

    Return the length of the longest substring
    containing the same letter you
    can get after performing the above operations.

    Example 1:

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's
    or vice versa.
    Example 2:

    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle
    with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating
    letters, which is 4.

    Constraints:

    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length
*/

package main

import "fmt"

// func characterReplacement(s string, k int) int {
//     var longest, slow, maxCount int
//     cCount := [26]int{}

//     for fast := 0; fast < len(s); fast++ {
//         cCount[s[fast]-'A']++
//         maxCount = max(maxCount, cCount[s[fast]-'A'])

//         for (fast - slow + 1) > (k + maxCount) {
//             cCount[s[slow]-'A']--
//             slow++
//         }

//         longest = max(longest, fast - slow + 1)
//     }

//     return longest
// }

// func characterReplacement(s string, k int) int {
//     wCount := map[byte]int{}
//     longest := 0
//     l, r := 0, 0

//     for r < len(s) {
//         wCount[s[r]]++
//         h := highest(wCount)
//         for (r - l + 1) > (wCount[h] + k)  {
//             wCount[s[l]]--
//             l++
//             h = highest(wCount)
//         }
//         longest = max(longest, r - l + 1)
//         r++
//     }

//     return longest
// }

// func highest(m map[byte]int) byte {
//     cnt := 0
//     var best byte 
//     for k, v := range m {
//         if v > cnt {
//             cnt = v
//             best = k
//         }
//     }

//     return best
// }

func characterReplacement(s string, k int) int {
    wCount := map[byte]int{}
    longest, maxCnt := 0, 0
    l, r := 0, 0

    for r < len(s) {
        wCount[s[r]]++
        maxCnt = max(maxCnt, wCount[s[r]])

        for (r - l + 1) > (maxCnt + k)  {
            wCount[s[l]]--
            l++
        }

        longest = max(longest, r - l + 1)
        r++
    }

    return longest
}


func main() {
	fmt.Println(characterReplacement("ABAB", 2))
	fmt.Println(lengthOfLongestSubstring("AABABBA", 1))
}

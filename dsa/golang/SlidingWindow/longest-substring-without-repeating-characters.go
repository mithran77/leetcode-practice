/*
	3. Longest Substring Without Repeating Characters

	Given a string s, find the length of the longest substring
	without repeating characters.

	Example 1:

	Input: s = "abcabcbb"
	Output: 3
	Explanation: The answer is "abc", with the length of 3.
	Example 2:

	Input: s = "bbbbb"
	Output: 1
	Explanation: The answer is "b", with the length of 1.
	Example 3:

	Input: s = "pwwkew"
	Output: 3
	Explanation: The answer is "wke", with the length of 3.
	Notice that the answer must be a substring, "pwke" is a
	subsequence and not a substring.

	Constraints:

	0 <= s.length <= 5 * 104
	s consists of English letters, digits, symbols and spaces.
*/

package main

import "fmt"

// func lengthOfLongestSubstring(s string) int {
//     window := map[rune]struct{}{}
//     longest, l := 0, 0

//     for r, c := range s {
//         _, exists := window[c]
//         for exists {
//             delete(window, rune(s[l]))
//             l++
//             _, exists = window[c]
//         }

//         window[c] = struct{}{}
//         longest = max(longest, r - l + 1)
//     }

//     return longest
// }


func lengthOfLongestSubstring(s string) int {
    window := map[rune]int{}
    longest, l := 0, 0

    for r, c := range s {
        if i, exists := window[c]; exists {
            l = max(l, i + 1)
        } 

        window[c] = r
        longest = max(longest, r - l + 1)
    }

    return longest
}


func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
	fmt.Println(lengthOfLongestSubstring("bbbbb"))
	fmt.Println(lengthOfLongestSubstring("pwwkew"))
}

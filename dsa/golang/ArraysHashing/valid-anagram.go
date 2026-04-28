/*

# 242. Valid Anagram
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you
# adapt your solution to such a case?

*/

package main

import "fmt"

// func isAnagram(s string, t string) bool {
// 	if len(s) != len(t) {
// 		return false
// 	}
// 	count := make(map[string]int)
// 	for _, val := range s {
// 		_, ok := count[string(val)]
// 		if ok {
// 			count[string(val)] = count[string(val)] + 1
// 		} else {
// 			count[string(val)] = 1
// 		}
// 	}
// 	for _, val := range t {
// 		_, ok := count[string(val)]
// 		if ok {
// 			count[string(val)] = count[string(val)] - 1
// 		} else {
// 			return false
// 		}
// 		if count[string(val)] == 0 {
// 			delete(count, string(val))
// 		}
// 	}
// 	if len(count) == 0 {
// 		return true
// 	}
// 	return false
// }

func isAnagram(s string, t string) bool {

    if len(s) != len(t) {
        return false
    }

    count := make([]int, 26)

    for i, _ := range s {
        count[s[i]-'a']++
        count[t[i]-'a']--
    }

    for _, c := range count {
        if c != 0 {
            return false
        }
    }

    return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
}

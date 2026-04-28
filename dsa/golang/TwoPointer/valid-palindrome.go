/*
# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads
# the same forward and backward. Alphanumeric characters include letters
# and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters. Since an empty string reads the same forward and backward,
# it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
*/

package main

import (
	"fmt"
	"strings"
	"unicode"
)

// func isPalindrome(s string) bool {
// 	if len(s) < 2 {
// 		return false
// 	}

// 	i, j := 0, len(s)-1
// 	for i < j {
// 		if (s[i] < 'a' || s[i] > 'z') && (s[i] < 'A' || s[i] > 'Z') {
// 			i++
// 			continue
// 		} else if (s[j] < 'a' || s[j] > 'z') && (s[j] < 'A' || s[j] > 'Z') {
// 			j--
// 			continue
// 		}
// 		if strings.ToLower(string(s[i])) != strings.ToLower(string(s[j])) {
// 			return false
// 		}
// 		i++
// 		j--
// 	}
// 	return true
// }

// func isPalindrome(s string) bool {
// 	f := func(r rune) rune {
// 		if !unicode.IsLetter(r) && !unicode.IsNumber(r) {
// 			return -1
// 		}

// 		return unicode.ToLower(r)
// 	}
// 	s = strings.Map(f, s)
// 	i, j := 0, len(s)-1
// 	for i < j {
// 		if s[i] != s[j] {
// 			return false
// 		}
// 		i++
// 		j--
// 	}
// 	return true
// }

// func isPalindrome(s string) bool {
// 	alphaNumericRegex := regexp.MustCompile(`[^a-zA-Z0-9]+`)
// 	s = alphaNumericRegex.ReplaceAllString(s, "")
// 	s = strings.ToLower(s)
// 	i, j := 0, len(s)-1
// 	for i < j {
// 		if s[i] != s[j] {
// 			return false
// 		}
// 		i++
// 		j--
// 	}
// 	return true
// }

func isPalindrome(s string) bool {
    l, r := 0, len(s) - 1

    for l < r {
        for l < r && !isAlphaNumeric(rune(s[r])) {
            r--
        }
        for l < r && !isAlphaNumeric(rune(s[l])) {
            l++
        }

        if unicode.ToLower(rune(s[r])) != unicode.ToLower(rune(s[l])) {
            return false
        }

        l++
        r--
    }

    return true
}

func isAlphaNumeric(c rune) bool {
    return unicode.IsLetter(c) || unicode.IsDigit(c)
}

func main() {
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println(isPalindrome("0P"))
}

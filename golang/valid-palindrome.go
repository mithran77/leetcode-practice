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

func isPalindrome(s string) bool {
	f := func(r rune) rune {
		if !unicode.IsLetter(r) && !unicode.IsNumber(r) {
			return -1
		}

		return unicode.ToLower(r)
	}
	s = strings.Map(f, s)
	i, j := 0, len(s)-1
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}

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

func main() {
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println(isPalindrome("0P"))
}

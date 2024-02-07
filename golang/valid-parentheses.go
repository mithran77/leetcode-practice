package main

import (
	"fmt"

	"golang.org/x/exp/slices"
)

// func isValid(s string) bool {
// 	if len(s) == 0 || len(s)%2 == 1 {
// 		return false
// 	}

// 	bracketStack := []string{}

// 	bracketMap := map[rune]rune{
// 		')': '(',
// 		'}': '{',
// 		']': '[',
// 	}
// 	for i := 0; i < len(s); i++ {
// 		if s[i] == '(' || s[i] == '{' || s[i] == '[' {
// 			bracketStack = append(bracketStack, string(s[i]))
// 			continue
// 		}
// 		if s[i] == ')' {
// 			if bracketStack[len(bracketStack)-1] != "(" {
// 				return false
// 			}
// 		} else if s[i] == '}' {
// 			if bracketStack[len(bracketStack)-1] != "{" {
// 				return false
// 			}
// 		} else if s[i] == ']' {
// 			if bracketStack[len(bracketStack)-1] != "[" {
// 				return false
// 			}
// 		}
// 		bracketStack = bracketStack[:len(bracketStack)-1]
// 	}
// 	return len(bracketStack) == 0
// }

func isValid(s string) bool {
	bracketStack := []string{}
	bracketMap := map[string]string{
		")": "(",
		"}": "{",
		"]": "[",
	}
	var keys []string
	for k := range bracketMap {
		keys = append(keys, k)
	}
	var values []string
	for _, v := range bracketMap {
		values = append(values, v)
	}
	for _, v := range s {
		if slices.Contains(keys, string(v)) {
			if len(bracketStack) > 0 && bracketStack[len(bracketStack)-1] == bracketMap[string(v)] {
				bracketStack = bracketStack[:len(bracketStack)-1]
			} else {
				return false
			}
		} else {
			bracketStack = append(bracketStack, string(v))
		}
	}
	return len(bracketStack) == 0
}

func main() {
	fmt.Println(isValid("()"))
}

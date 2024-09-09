package main

import "fmt"

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	count := make(map[string]int)
	for _, val := range s {
		_, ok := count[string(val)]
		if ok {
			count[string(val)] = count[string(val)] + 1
		} else {
			count[string(val)] = 1
		}
	}
	for _, val := range t {
		_, ok := count[string(val)]
		if ok {
			count[string(val)] = count[string(val)] - 1
		} else {
			return false
		}
		if count[string(val)] == 0 {
			delete(count, string(val))
		}
	}
	if len(count) == 0 {
		return true
	}
	return false
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
}

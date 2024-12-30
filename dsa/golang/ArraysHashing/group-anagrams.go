package main

import "fmt"

// Maps of Array
func groupAnagrams(strs []string) [][]string {
	arrMap := map[[26]int][]string{}
	for _, s := range strs {
		tmpKey := [26]int{}
		for _, s := range s {
			tmpKey[s-'a']++
		}
		arrMap[tmpKey] = append(arrMap[tmpKey], s)
	}
	res := [][]string{}
	for _, v := range arrMap {
		res = append(res, v)
	}
	return res
}

func main() {
	fmt.Println([]string{"eat", "tea", "tan", "ate", "nat", "bat"})
}

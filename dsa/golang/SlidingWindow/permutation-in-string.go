/*
    567. Permutation in String

    Given two strings s1 and s2, return true if s2
    contains a permutation of s1, or false otherwise.
    In other words, return true if one of s1's
    permutations is the substring of s2.

    Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").

    Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

    Constraints:
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
*/

package main

import "fmt"

// BF
// func checkInclusion(s1 string, s2 string) bool {
//     s1Cnt := map[byte]int{}
//     for i := range s1 {
//         s1Cnt[s1[i]]++
//     }

//     for f := 0; f < len(s2); f++ {

//         if _, exists := s1Cnt[s2[f]]; exists {
//             wCnt := map[byte]int{}
//             for i := 0; i < len(s1) && (f + i) < len(s2); i++ {
//                 // Grow & check for match
//                 wCnt[s2[f+i]]++
//             }

//             if isEqual(s1Cnt, wCnt) {
//                 return true
//             }

//         }

//     }

//     return false
// }

// func isEqual(a, b map[byte]int) bool {

//     if len(a) != len(b) {
//         return false
//     }

//     for k, v := range a {
//         if b[k] != v {
//             return false
//         }
//     }

//     return true
// }

// Without fully optimized tricks

// func checkInclusion(s1 string, s2 string) bool {
//     s1Cnt := map[byte]int{}
//     for i := range s1 {
//         s1Cnt[s1[i]]++
//     }

//     wCnt := map[byte]int{}
//     for f := 0; f < len(s2); f++ {

//         if f >= len(s1) {
//             wCnt[s2[f-len(s1)]]--
//             if wCnt[s2[f-len(s1)]] == 0 {
//                 delete(wCnt, s2[f-len(s1)])
//             }
//         }

//         wCnt[s2[f]]++
//         if isEqual(s1Cnt, wCnt) {
//             return true
//         }

//     }

//     return false
// }

// func isEqual(a, b map[byte]int) bool {

//     if len(a) != len(b) {
//         return false
//     }

//     for k, v := range a {
//         if b[k] != v {
//             return false
//         }
//     }

//     return true
// }

func checkInclusion(s1 string, s2 string) bool {

    if len(s2) < len(s1) {
        return false
    }

    s1Count := map[byte]int{}
    wCount := map[byte]int{}
    for f := 0; f < len(s1); f++ {
        s1Count[s1[f]]++
        wCount[s2[f]]++
    }

    if equalMaps(s1Count, wCount) {
        return true
    }

    for f := len(s1); f < len(s2); f++ {
        s := f-len(s1)
        wCount[s2[f]]++
        wCount[s2[s]]--

        if equalMaps(s1Count, wCount) {
            return true
        }
    }

    return false
}

func equalMaps(a, b map[byte]int) bool {

    for k, v := range(a) {
        if b[k] != v {
            return false
        }
    }

    return true

}

func main() {
	fmt.Println(checkInclusion("ab", "eidbaooo"))
	fmt.Println(checkInclusion("ab", "eidboaoo"))
}

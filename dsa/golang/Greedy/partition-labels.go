/*
    763. Partition Labels

    You are given a string s. We want to partition
    the string into as many parts as possible so
    that each letter appears in at most one part.

    Note that the partition is done so that after
    concatenating all the parts in order, the
    resultant string should be s.

    Return a list of integers representing the
    size of these parts.

    Example 1:
    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde",
    "hijhklij".
    This is a partition so that each letter
    appears in at most one part.
    A partition like "ababcbacadefegde",
    "hijhklij" is incorrect, because it splits
    s into less parts.

    Example 2:
    Input: s = "eccbbbbdec"
    Output: [10]


    Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
*/

func partitionLabels(s string) []int {
    freqCount := map[rune]int{}
    for _, c := range s {
        freqCount[c]++
    }

    curSet := map[rune]struct{}{}
    res := []int{}
    start := 0

    for i, c := range s {
        curSet[c] = struct{}{}    
        freqCount[c]--
        if freqCount[c] == 0 {
            delete(freqCount, c)
            delete(curSet, c)
        }
        if len(curSet) == 0 {
            res = append(res, i - start + 1)
            start = i + 1
        }
    }

    return res
}


func partitionLabels(s string) []int {
    lastIdx := map[rune]int{}
    for i, c := range s {
        lastIdx[c] = i
    }

    res := []int{}
    end, count := 0, 0

    for i, c := range s {
        count++
        end = max(end, lastIdx[c])
        if i == end {
            res = append(res, count)
            count = 0
        }
    }

    return res
}
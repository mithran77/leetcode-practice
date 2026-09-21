/*

    846. Hand of Straights

    Alice has some number of cards and she wants
    to rearrange the cards into groups so that
    each group is of size groupSize, and consists
    of groupSize consecutive cards. Given an integer
    array hand where hand[i] is the value written
    on the ith card and an integer groupSize, return
    true if she can rearrange the cards, or false
    otherwise.

    Example 1:
    Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
    Output: true
    Explanation: Alice's hand can be rearranged as
    [1,2,3],[2,3,4],[6,7,8]

    Example 2:
    Input: hand = [1,2,3,4,5], groupSize = 4
    Output: false
    Explanation: Alice's hand can not be rearranged
    into groups of 4.

    Constraints:
    1 <= hand.length <= 104
    0 <= hand[i] <= 109
    1 <= groupSize <= hand.length

    Note: This question is the same as 1296:
    https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

*/

func isNStraightHand(hand []int, groupSize int) bool {
    if len(hand) % groupSize != 0 {
        return false
    }
    slices.Sort(hand)

    r := 0
    for r < len(hand) {
        start := hand[r]
        for i := range groupSize {
            idx := slices.Index(hand, start + i)
            if idx != -1 {
                hand = slices.Delete(hand, idx, idx + 1)
            } else {
                return false
            }
        }
    }

    return len(hand) == 0
}


func isNStraightHand(hand []int, groupSize int) bool {
    if len(hand)%groupSize != 0 {
        return false
    }
    slices.Sort(hand)

    for r := 0; r < len(hand); r++ {
        if hand[r] == -1 {
            continue
        }
        need := hand[r]
        cnt := 0
        for j := r; j < len(hand) && cnt < groupSize; j++ {
            if hand[j] == need {
                hand[j] = -1
                need++
                cnt++
            }
        }
        if cnt != groupSize {
            return false
        }
    }

    for _, h := range hand {
        if h != -1 {
            return false
        }
    }

    return true
}

// Greedy
func isNStraightHand(hand []int, groupSize int) bool {
    freqCount := map[int]int{}
    for _, h := range hand {
        freqCount[h]++
    }

    for _, num := range hand {
        start := num
        if _, exists := freqCount[start]; !exists {
            continue
        }
        for freqCount[start - 1] > 0 {
            start--
        }

        for start <= num {
            _, canStart := freqCount[start]
            for canStart {
                for i := range groupSize {
                    if _, exists := freqCount[start + i]; !exists {
                        return false
                    }
                    freqCount[start + i]--
                    if freqCount[start + i] == 0 {
                        delete(freqCount, start + i)
                    }
                }
                _, canStart = freqCount[start]
            }
            start++
        }

    }

    return len(freqCount) == 0
}

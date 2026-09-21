/*
    678. Valid Parenthesis String

    Given a string s containing only three
    types of characters: '(', ')' and '*',
    return true if s is valid.

    The following rules define a valid string:

    Any left parenthesis '(' must have a
    corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a
    corresponding left parenthesis '('.
    Left parenthesis '(' must go before the
    corresponding right parenthesis ')'.
    '*' could be treated as a single right
    parenthesis ')' or a single left parenthesis
    '(' or an empty string "".

    Example 1:
    Input: s = "()"
    Output: true

    Example 2:
    Input: s = "(*)"
    Output: true

    Example 3:
    Input: s = "(*))"
    Output: true

    Constraints:
    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.
*/

// Stack
func checkValidString(s string) bool {
    stOpen, stStar := []int{}, []int{}

    for i, c := range s {
        switch c {
            case '(':
                stOpen = append(stOpen, i)
                break
            case '*':
                stStar = append(stStar, i)
                break
            case ')':
                if len(stOpen) == 0 && len(stStar) == 0 {
                    return false
                } else if len(stOpen) > 0 {
                    stOpen = stOpen[:len(stOpen) - 1]
                } else {
                    stStar = stStar[:len(stStar) - 1]
                }
        }
    }

    for len(stOpen) > 0 && len(stStar) > 0 {
        oLen, sLen := len(stOpen), len(stStar)
        openIdx, starIdx := stOpen[oLen - 1], stStar[sLen - 1]
        if openIdx > starIdx {
            return false
        }
        stOpen, stStar = stOpen[:oLen - 1], stStar[:sLen - 1]
    }

    return len(stOpen) == 0
}

// Greedy
func checkValidString(s string) bool {
    openMin, openMax := 0, 0

    for _, c := range s {
        switch c {
            case '(':
                openMin++; openMax++
            case ')':
                openMin--; openMax--
            case '*':
                openMin--; openMax++
        }
        if openMax < 0 {
            return false
        }
        if openMin < 0 {
            openMin = 0
        }
    }

    return openMin == 0
}
/*

	20. Valid Parentheses

	Given a string s containing just the characters
	'(', ')', '{', '}', '[' and ']', determine if
	the input string is valid.

	An input string is valid if:

	Open brackets must be closed by the same type of
	brackets. Open brackets must be closed in the
	correct order.


	Example 1:
	Input: s = "()"
	Output: true

	Example 2:
	Input: s = "()[]{}"
	Output: true

	Example 3:
	Input: s = "(]"
	Output: false


	Constraints:
	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.

*/

package main

func isValid(s string) bool {
    closeToOpen := map[rune]rune{   // S: O(6)
        ')': '(',
        ']': '[',
        '}': '{',
    }
    
    stack := []rune{}               // S: O(n)
    for _, brace := range s {       // T: O(n)
        if open, isClose := closeToOpen[brace]; isClose {
            sLen := len(stack)
            if sLen < 1 || stack[sLen-1] != open {
                return false
            } else {
                stack = stack[:sLen-1]
            }
        } else {
            stack = append(stack, brace)
        }

    }

    return len(stack) == 0
}

func main() {
	fmt.Println(isValid("()"))
}

/*
#
# https://www.lintcode.com/problem/659/
# https://leetcode.com/problems/encode-and-decode-strings/description/
# https://neetcode.io/problems/string-encode-and-decode
#
# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.
#
# Please implement encode and decode
#
# Example 1:
#
# Input: ["neet","code","love","you"]
#
# Output:["neet","code","love","you"]
# Example 2:
#
# Input: ["we","say",":","yes"]
#
# Output: ["we","say",":","yes"]
# Constraints:
#
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.
#
*/

type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	encoded := ""

	for _, w := range strs {
		encoded += fmt.Sprintf("%d#%s", len(w), w)
	}

	return encoded
}

func (s *Solution) Decode(encoded string) []string {
	slow, fast := 0, 0
	decoded := []string{}

	for fast < len(encoded) {
		for encoded[fast] != '#' {
			fast++
		}

		l, _ := strconv.Atoi(encoded[slow:fast])

		slow = fast + 1
		fast = fast + l + 1

		decoded = append(decoded, encoded[slow:fast])
		slow = fast
	}

	return decoded
}

func main() {
    s := Solution{}
	fmt.Println(s.Encode([]string{"Hello","World"}))
    fmt.Println(s.Decode("Hello World"))
}

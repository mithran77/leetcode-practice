/*

    Alien Dictionary

    There is a new alien language that uses
    the English alphabet, but the order of
    the letters is unknown.

    You are given a list of strings words from
    the alien language's dictionary. It is
    claimed that the strings in words are
    sorted lexicographically by the rules of
    this new language.

    If this claim is incorrect, and the given
    arrangement of strings in words cannot
    correspond to any order of letters, return "".

    Otherwise, return a string of the unique
    letters in the new alien language sorted in
    lexicographically increasing order by the new
    language's rules. If there are multiple solutions,
    return any of them.

    A string a is lexicographically smaller than
    a string b if either of the following is true:

    The first letter where they differ is smaller
    in a than in b. a is a prefix of b and
    a.length < b.length.

    Example 1:
    Input: words = ["z","o"]
    Output: "zo"
    Explanation:
    From "z" and "o", we know 'z' < 'o', so return "zo".

    Example 2:
    Input: words = ["hrn","hrf","er","enn","rfnn"]
    Output: "hernf"
    Explanation:
    from "hrn" and "hrf", we know 'n' < 'f'
    from "hrf" and "er", we know 'h' < 'e'
    from "er" and "enn", we know 'r' < 'n'
    from "enn" and "rfnn" we know 'e' < 'r'
    so one possible solution is "hernf"

    Example 3:
    Input: words = ["abc","ab"]
    Output: ""
    Explanation:
    The second word is a prefix of the first word,
    but the first word appears before the second.
    This is impossible in a valid lexicographical
    ordering, so return "".

    Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of only lowercase English letters.

*/

func foreignDictionary(words []string) string {
    // Create adjacency list
	adj := map[byte][]byte{}
	for _, w := range words {
		for j := range w {
			adj[w[j]] = []byte{}
		}
	}

	for i := range len(words) - 1 {
		w1, w2 := words[i], words[i+1]
		wLen := min(len(w1), len(w2))

		j := 0
		for ; j < wLen; j++ {
			if w1[j] != w2[j] {
				adj[w1[j]] = append(adj[w1[j]], w2[j])
				break
			}
		}
		if j == wLen && len(w1) > len(w2) {
			return ""
		}
	}

	// Create in-degrees
	inDegrees := map[byte]int{}
	for k := range adj { inDegrees[k] = 0 }
	for _, v  := range adj {
		for _, n := range v {
			inDegrees[n]++
		}
	}

	queue := []byte{}
	for k, v := range inDegrees {
		if v == 0 {
			queue = append(queue, k)
		}
	}

	alphabet := []byte{}
	for len(queue) > 0 {
		l := queue[0]
		queue = queue[1:]

		alphabet = append(alphabet, l)
		for _, nei := range adj[l] {
			inDegrees[nei]--
			if inDegrees[nei] == 0 {
				queue = append(queue, nei)
			}
		}
	}

	for _, v := range inDegrees {
		if v != 0 {
			return ""
		}
	}

	return string(alphabet[:])
}

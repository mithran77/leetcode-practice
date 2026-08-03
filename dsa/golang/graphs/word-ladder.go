/*

    127. Word Ladder

    A transformation sequence from word
    beginWord to word endWord using a dictionary
    wordList is a sequence of words 
    beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by
    a single letter.
    Every si for 1 <= i <= k is in wordList.
    Note that beginWord does not need to be in wordList.
    sk == endWord
    Given two words, beginWord and endWord,
    and a dictionary wordList,
    return the number of words in the shortest
    transformation sequence from beginWord to
    endWord, or 0 if no such sequence exists.

    Example 1:
    Input: beginWord = "hit", endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation
    sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog",
    which is 5 words long.

    Example 2:
    Input: beginWord = "hit", endWord = "cog",
    wordList = ["hot","dot","dog","lot","log"]
    Output: 0
    Explanation: The endWord "cog" is not in wordList,
    therefore there is no valid transformation sequence.


    Constraints:
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of
    lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.

*/

func ladderLength(beginWord string, endWord string, wordList []string) int {
    // Base case
    if !slices.Contains(wordList, endWord) {
        return 0
    }

    // Create adjacency list
    wordList = append(wordList, beginWord)
    adj := map[string][]string{}
    for _, w := range wordList {
        for i := range len(w) {
            pattern := fmt.Sprintf("%s%s%s", w[:i], "*", w[i+1:])
            adj[pattern] = append(adj[pattern], w)
        }
    }

    q := []string{beginWord}
    visit := map[string]bool{}
    numberOfWords := 1
    // Perform BFS
    for len(q) > 0 {
        qLen := len(q)
        for range qLen {
            w := q[0]
            q = q[1:]
            for i := range len(w) {
                pattern := fmt.Sprintf("%s%s%s", w[:i], "*", w[i+1:])
                for _, nei := range adj[pattern] {
                    if nei == w {
                        continue
                    }
                    if _, visited := visit[nei]; visited {
                        continue
                    }
                    if nei == endWord {
                        return numberOfWords + 1
                    }
                    q = append(q, nei)
                }
            }
            visit[w] = true
        }
        numberOfWords++
    }

    return 0
}


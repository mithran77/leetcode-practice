/*
    212. Word Search II

    Given an m x n board of characters
    and a list of strings words, return
    all words on the board.

    Each word must be constructed from
    letters of sequentially adjacent cells,
    where adjacent cells are horizontally
    or vertically neighboring. The same
    letter cell may not be used more than
    once in a word.

    Example 1:
    Input: board = [["o","a","a","n"],
    ["e","t","a","e"],["i","h","k","r"],
    ["i","f","l","v"]],
    words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

    Example 2:
    Input: board = [["a","b"],["c","d"]],
    words = ["abcb"]
    Output: []

    Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English
    letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English
    letters.
    All the strings of words are unique.

*/

import "maps"

type TrieNode struct {
    children map[rune]*TrieNode
    isWord bool
}

func newTrieNode() *TrieNode {
    return &TrieNode{
        children: map[rune]*TrieNode{},
    }
}

func (t *TrieNode) addWords(word string) {
    node := t
    for _, l := range word {
        _, exists := node.children[l]
        if !exists {
            node.children[l] = newTrieNode()
        }
        node = node.children[l]
    }
    node.isWord = true
}

func findWords(board [][]byte, words []string) []string {
    root := newTrieNode()
    for _, w := range words { root.addWords(w) }

    rows, cols := len(board), len(board[0])
    visit := map[[2]int]bool{}
    wordSet := map[string]struct{}{}

    var dfs func(r int, c int, node *TrieNode, word string)
    dfs = func(r int, c int, node *TrieNode, word string) {
        if 0 > r || r >= rows || 0 > c || c >= cols || visit[[2]int{r, c}] {
            return
        }

        char := rune(board[r][c])
        nextNode, exists := node.children[char]
        if !exists {
            return
        }

        visit[[2]int{r,c}] = true
        defer func() {visit[[2]int{r,c}] = false}()

        word += string(char)
        if nextNode.isWord {
            wordSet[word] = struct{}{}
        }

        dfs(r - 1, c, nextNode, word)
        dfs(r + 1, c, nextNode, word)
        dfs(r, c - 1, nextNode, word)
        dfs(r, c + 1, nextNode, word)

    }

    for r := range rows {
        for c := range cols {
            dfs(r, c, root, "")
        }
    }

    return slices.Collect(maps.Keys(wordSet))

}


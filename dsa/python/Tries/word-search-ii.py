# 212. Word Search II

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.

# Example 1:

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

from typing import List

# # Brute Force
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         found = set([])
#         ROWS, COLS = len(board), len(board[0])
#         visited = set()

#         def backtrack(r, c, word, i):
#             if i == len(word):
#                 return True
#             if (r not in range(ROWS) or
#                 c not in range(COLS) or
#                 i > len(word) or
#                 board[r][c] != word[i] or
#                 (r, c) in visited):
#                 return False

#             visited.add((r, c))
#             res = (
#                 backtrack(r + 1, c, word, i + 1) or
#                 backtrack(r - 1, c, word, i + 1) or
#                 backtrack(r, c + 1, word, i + 1) or
#                 backtrack(r, c - 1, word, i + 1)
#             )

#             visited.remove((r, c))
#             return res

#         for w in words:
#             for r in range(ROWS):
#                 for c in range(COLS):
#                     if w not in found and board[r][c] == w[0]:
#                         if backtrack(r, c, w, 0):
#                             found.add(w)

#         return list(found)

# Create Trie First, then search

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Add words to trie
        for w in words:
            root.insert(w)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visited or
                board[r][c] not in node.children):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end_of_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))

        # Traverse board while matching elements in try.
        # Backtrack when word not found along trie path
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

if __name__ == '__main__':
    res = Solution()
    print(res.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))
    print(res.findWords(board = [["a","b"],["c","d"]], words = ["abcb"]))


# Time & Space Complexity

# Time complexity: O(m∗n∗4∗3 t−1 +s)
# Space complexity:  O(s)

# Where m is the number of rows, n is the number of columns,
# t is the maximum length of any word in the array words and
# s is the sum of the lengths of all the words.

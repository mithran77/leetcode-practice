class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            cur = node
            for j in range(i, len(word)):
                c = word[j]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(child, j+1):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.word

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

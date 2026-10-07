/*

    211. Design Add and Search Words
    Data Structure

    Design a data structure that supports
    adding new words and finding if a
    string matches any previously added
    string.

    Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the
    data structure, it can be matched later.
    bool search(word) Returns true if
    there is any string in the data structure
    that matches word or false otherwise.
    word may contain dots '.' where dots can
    be matched with any letter.


    Example:
    Input
    ["WordDictionary","addWord","addWord",
    "addWord","search","search","search",
    "search"]
    [[],["bad"],["dad"],["mad"],["pad"],
    ["bad"],[".ad"],["b.."]]
    Output
    [null,null,null,null,false,true,true,true]

    Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True


    Constraints:
    1 <= word.length <= 25
    word in addWord consists of lowercase
    English letters.
    word in search consist of '.' or lowercase
    English letters.
    There will be at most 2 dots in word for
    search queries.
    At most 104 calls will be made to addWord
    and search.

*/

// Wierd (uses WordDictionary)
type TrieNode struct {
    children map[rune]*TrieNode
    isWord bool
}

type WordDictionary struct {
    root *TrieNode
}


func Constructor() WordDictionary {
    return WordDictionary{
        root: &TrieNode{
            children: map[rune]*TrieNode{},
        },
    }
}


func (w *WordDictionary) AddWord(word string)  {
    node := w.root
    for _, l := range word {
        if _, exists := node.children[l]; !exists {
            node.children[l] = &TrieNode{
                children: map[rune]*TrieNode{},
            }
        }
        node = node.children[l]
    }
    node.isWord = true
}


func (w *WordDictionary) Search(word string) bool {
    node := w.root
    for i, l := range word {
        if l == '.' {
            for _, child := range node.children {
                if (&WordDictionary{root: child}).Search(word[i+1:]) {
                    return true
                } 
            }
            return false
        }
        if _, exists := node.children[l]; !exists {
            return false
        }
        node = node.children[l]
    }
    return node.isWord
}


// Seperate DFS
type TrieNode struct {
    children map[rune]*TrieNode
    endOfWord bool
}

type WordDictionary struct {
    root *TrieNode
}


func Constructor() WordDictionary {
    return WordDictionary{
        root: &TrieNode{
            children: map[rune]*TrieNode{},
        },
    }
}


func (w *WordDictionary) AddWord(word string)  {
    node := w.root
    for _, l := range word {
        if _, exists := node.children[l]; !exists {
            node.children[l] = &TrieNode{
                children: map[rune]*TrieNode{},
            }
        }
        node = node.children[l]
    }
    node.endOfWord = true
}


func (w *WordDictionary) Search(word string) bool {
    return w.dfs(word, w.root)
}

func (w *WordDictionary) dfs(word string, node *TrieNode) bool {
    for i, l := range word {
        if l == '.' {
            for _, child := range node.children {
                if w.dfs(word[i+1:], child) {
                    return true
                } 
            }
            return false
        }
        if _, exists := node.children[l]; !exists {
            return false
        }
        node = node.children[l]
    }
    return node.endOfWord
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */


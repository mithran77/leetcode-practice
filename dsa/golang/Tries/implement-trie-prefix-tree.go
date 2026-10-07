/*
    208. Implement Trie (Prefix Tree)

    A trie (pronounced as "try") or
    prefix tree is a tree data structure
    used to efficiently store and
    retrieve keys in a dataset of strings.
    There are various applications
    of this data structure, such as
    autocomplete and spellchecker.

    Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the
    string word into the trie. boolean
    search(String word) Returns true if
    the string word is in the trie
    (i.e., was inserted before), and false
    otherwise. boolean startsWith(String prefix)
    Returns true if there is a previously
    inserted string word that has the prefix
    prefix, and false otherwise.

    Example 1:
    Input
    ["Trie", "insert", "search", "search",
    "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"],
    ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]

    Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True

    Constraints:
    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase
    English letters. At most 3 * 104 calls in
    total will be made to insert, search, and
    startsWith.
*/

// Array

type TrieNode struct {
    children [26]*TrieNode
    isWord bool
}

type Trie struct {
    root *TrieNode
}

func Constructor() Trie {
    return Trie{root: &TrieNode{
        children: [26]*TrieNode{},
    }}
}

func (t *Trie) Insert(word string)  {
    node := t.root
    for _, l := range word {
        if node.children[l-'a'] == nil {
            node.children[l-'a'] = &TrieNode{
                children: [26]*TrieNode{},
            }
        }
        node = node.children[l-'a']
    }
    node.isWord = true
}


func (t *Trie) Search(word string) bool {
    node := t.root
    for _, l := range word {
        if node.children[l-'a'] == nil {
            return false
        }
        node = node.children[l-'a']
    }
    return node.isWord
}


func (t *Trie) StartsWith(prefix string) bool {
    node := t.root
    for _, l := range prefix {
        if node.children[l-'a'] == nil {
            return false
        }
        node = node.children[l-'a']
    }
    return true
}


// Map
type TrieNode struct {
    children map[rune]*TrieNode
    isWord bool
}

type Trie struct {
    root *TrieNode
}

func Constructor() Trie {
    return Trie{root: &TrieNode{
        children: map[rune]*TrieNode{},
    }}
}

func (t *Trie) Insert(word string)  {
    node := t.root
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


func (t *Trie) Search(word string) bool {
    node := t.root
    for _, l := range word {
        if _, exists := node.children[l]; !exists {
            return false
        }
        node = node.children[l]
    }
    return node.isWord
}


func (t *Trie) StartsWith(prefix string) bool {
    node := t.root
    for _, l := range prefix {
        if _, exists := node.children[l]; !exists {
            return false
        }
        node = node.children[l]
    }
    return true
}


// Your Trie object will be instantiated and called as such:
// obj = Trie()
// obj.insert(word)
// param_2 = obj.search(word)
// param_3 = obj.startsWith(prefix)

// Time complexity: O(n) for each function call.
// Space complexity: O(t)
// Where n is the length of the string and t is the total number of
// TrieNodes created in the Trie

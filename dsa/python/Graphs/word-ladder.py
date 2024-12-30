# 127. Word Ladder

# A transformation sequence from word beginWord to word endWord using a dictionary wordList
# is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList,
# return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


from typing import List
from collections import defaultdict, deque

# # TLE (Adj + BFS)
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         # Create adjacency list
#         adj = defaultdict(list)

#         def differsByOne(w1, w2):
#             cnt = 0
#             for i in range(len(w1)):
#                 if w1[i] != w2[i]:
#                     cnt += 1
#             return cnt == 1

#         for w1 in ([beginWord] + wordList):
#             for w2 in wordList:
#                 if differsByOne(w1, w2):
#                     adj[w1].append(w2)
#                     adj[w2].append(w1)

#         # BFS
#         visit = set()
#         res = 1
#         q = deque([beginWord])

#         while q:
#             for _ in range(len(q)):

#                 e = q.popleft()
#                 if e == endWord:
#                     return res

#                 visit.add(e)
#                 for n in adj[e]:
#                     if n not in visit:
#                         q.append(n)

#             res += 1

#         return 0


# Adj + BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        # Create adjacency list
        adj = defaultdict(list)
        wordList.append(beginWord)
        for w in (wordList):
            for j in range(len(w)):
                pattern = w[:j] + '*' + w[j+1:]
                adj[pattern].append(w)

        # BFS
        visit = set()
        res = 1
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):

                w = q.popleft()
                if w == endWord:
                    return res

                for j in range(len(w)):
                    pattern = w[:j] + '*' + w[j+1:]
                    for n in adj[pattern]:
                        if n not in visit:
                            visit.add(n)
                            q.append(n)

            res += 1

        return 0

if __name__ == '__main__':
    ans = Solution()
    print(ans.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
    print(ans.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))


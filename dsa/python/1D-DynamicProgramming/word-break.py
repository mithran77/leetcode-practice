# 139. Word Break
# Medium
# Topics
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

from typing import List

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True

#         for i in range(len(s) - 1, -1, -1):
#             for w in wordDict:
#                 if i + len(w) <= len(s) and s[i : i + len(w)] == w:
#                     dp[i] = dp[i + len(w)]
#                 if dp[i]:
#                     break

#         return dp[0]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = [-1] * len(s)

        def rWordBreak(i:int)->bool:
            if i == len(s):
                return True
            if memo[i] != -1:
                return memo[i]

            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if rWordBreak(i=(i+len(w))):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return rWordBreak(i=0)


if __name__ == '__main__':
    ans = Solution()
    print(ans.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
    print(ans.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
    print(ans.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))


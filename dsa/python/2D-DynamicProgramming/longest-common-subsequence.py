# 1143. Longest Common Subsequence

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without
# changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

# Constraints:
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

from typing import List

# Memo
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [
            [-1] * (len(text2))
            for _ in range(len(text1))
        ]

        def rLCS(idx1, idx2):

            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]

            # BC
            if idx1 < 0 or idx2 < 0:
                return 0

            if text1[idx1] == text2[idx2]:
                dp[idx1][idx2] = 1 + rLCS(idx1-1, idx2-1)
            else:
                dp[idx1][idx2] = max(rLCS(idx1-1, idx2), rLCS(idx1, idx2-1))

            return dp[idx1][idx2]

        return rLCS(len(text1)-1, len(text2)-1)


# # Tabulation
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # Right shift DP array
#         dp = [
#             [0] * (len(text2)+1)
#             for _ in range(len(text1)+1)
#         ]

#         for r in range(1, len(text1)+1):
#             for j in range(1, len(text2)+1):
#                 if text1[r-1] == text2[j-1]:
#                     dp[r][j] = 1 + dp[r-1][j-1]
#                 else:
#                     dp[r][j] = max(dp[r-1][j], dp[r][j-1])


#         return dp[len(text1)][len(text2)]


if __name__ == '__main__':
    ans = Solution()
    print(ans.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
    print(ans.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(ans.longestCommonSubsequence(text1 = "abc", text2 = "def"))


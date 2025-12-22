# https://www.geeksforgeeks.org/problems/longest-common-substring1452/1
# You are given two strings s1 and s2. Your task is to find the length of the longest common substring among the given strings.

# Examples:

# Input: s1 = "ABCDGH", s2 = "ACDGHR"
# Output: 4
# Explanation: The longest common substring is "CDGH" with a length of 4.

# Input: s1 = "abc", s2 = "acb"
# Output: 1
# Explanation: The longest common substrings are "a", "b", "c" all having length 1.

# Input: s1 = "YZ", s2 = "yz"
# Output: 0

# Constraints:
# 1 <= s1.size(), s2.size() <= 103
# Both strings may contain upper and lower case alphabets.


from typing import List


class Solution:
    def longestCommonSubstr(self, s1, s2):
        # Right shift DP array
        dp = [
            [0] * (len(s2)+1)
            for _ in range(len(s1)+1)
        ]

        ans = 0
        for r in range(1, len(s1)+1):
            for c in range(1, len(s2)+1):
                if s1[r-1] == s2[c-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                    ans = max(ans, dp[r][c])
                else:
                    dp[r][c] = 0

        return ans


if __name__ == '__main__':
    ans = Solution()
    print(ans.longestCommonSubstr(s1 = "ABCDGH", s2 = "ACDGHR"))
    print(ans.longestCommonSubstr(s1 = "abc", s2 = "acb"))
    print(ans.longestCommonSubstr(s1 = "YZ", s2 = "yz"))


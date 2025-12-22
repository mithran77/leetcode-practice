# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"


# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


from typing import List

# # Expand from possible centers
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         res = ""
#         res_len = 0

#         for i in range(len(s)):
#             # Odd length strings
#             l, r = i, i
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > res_len:
#                     res = s[l : r + 1]
#                     res_len = r - l + 1
#                 l -= 1
#                 r += 1

#             # Even length strings
#             l, r = i, i + 1
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > res_len:
#                     res = s[l : r + 1]
#                     res_len = r - l + 1
#                 l -= 1
#                 r += 1

#         return res

# Memoization
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        start, length = 0, 0

        dp = [
            [-1] * N
            for _ in range(N)
        ]

        def isPalindrome(i, j):
            if i >= j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]            

            if s[i] == s[j]:
                dp[i][j] = isPalindrome(i+1, j-1)
            else:
                dp[i][j] = 0

            return dp[i][j]


        for i in range(N):
            for j in range(i, N):
                if isPalindrome(i, j) == 1:
                    if j - i + 1 > length:
                        start = i
                        length = j - i + 1

        return s[start:start+length]

if __name__ == '__main__':
    res = Solution()
    print(res.longestPalindrome(s = "babad"))
    print(res.longestPalindrome(s = "cbbd"))


# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such
# that every character in t (including duplicates) is included in the window. If there is no such substring,
# return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

# Follow up: Could you find an algorithm that runs in O(m + n) time?

# from collections import Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not t or not s:
#             return ""

#         # Dictionary which keeps a count of all the unique characters in t.
#         dict_t = Counter(t)

#         # Number of unique characters in t, which need to be present in the desired window.
#         required = len(dict_t)

#         # left and right pointer
#         l, r = 0, 0

#         # formed is used to keep track of how many unique characters in t are present in the current 
#         # window in its desired frequency.
#         # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would 
#         # be = 3 when all these conditions are met.
#         formed = 0

#         # Dictionary which keeps a count of all the unique characters in the current window.
#         window_counts = {}

#         # ans tuple of the form (window length, left, right)
#         ans = float("inf"), None, None

#         while r < len(s):

#             # Add one character from the right to the window
#             character = s[r]
#             window_counts[character] = window_counts.get(character, 0) + 1

#             # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
#             if character in dict_t and window_counts[character] == dict_t[character]:
#                 formed += 1

#             # Try and contract the window till the point where it ceases to be 'desirable'.
#             while l <= r and formed == required:
#                 character = s[l]

#                 # Save the smallest window until now.
#                 if r - l + 1 < ans[0]:
#                     ans = (r - l + 1, l, r)

#                 # The character at the position pointed by the `left` pointer is no longer a part of the window.
#                 window_counts[character] -= 1
#                 if character in dict_t and window_counts[character] < dict_t[character]:
#                     formed -= 1

#                 # Move the left pointer ahead, this would help to look for a new window.
#                 l += 1

#             # Keep expanding the window once we are done contracting.
#             r += 1

#         return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


# from collections import Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not t or not s:
#             return ""

#         dict_t = Counter(t)

#         required = len(dict_t)
#         l, r = 0, 0
#         formed = 0
#         window_counts = {}

#         ans = float("inf"), None, None

#         while r < len(s):
#             character = s[r]
#             window_counts[character] = window_counts.get(character, 0) + 1

#             if character in dict_t and window_counts[character] == dict_t[character]:
#                 formed += 1

#             while l <= r and formed == required:
#                 character = s[l]

#                 if r - l + 1 < ans[0]:
#                     ans = (r - l + 1, l, r)

#                 window_counts[character] -= 1
#                 if character in dict_t and window_counts[character] < dict_t[character]:
#                     formed -= 1

#                 l += 1

#             r += 1

#         return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        ans, ans_len = "", len(s) + 1
        count_t, window = {}, {}
        l, r, have = 0, 0, 0

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1

            while have == len(count_t):
                if ans_len > (r - l + 1):
                    ans = s[l : r + 1]
                    ans_len = len(ans)

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.minWindow(s = "ADOBECODEBANC", t = "ABC"))
    print(res.minWindow(s = "a", t = "a"))
    print(res.minWindow(s = "a", t = "aa"))

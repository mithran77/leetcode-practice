# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other 
# uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         ans = rpos = lpos = 0
#         char_count = {}

#         while rpos < len(s):
#             r = s[rpos]
#             l = s[lpos]

#             if r not in char_count:
#                 char_count[r] = 0
#             char_count[r] += 1

#             cur_len = rpos - lpos + 1

#             if (cur_len - max(char_count.values())) <= k:
#                 ans = max(ans, cur_len)
#             else:
#                 char_count[l] -= 1
#                 if char_count[l] == 0:
#                     del char_count[l]
#                 lpos += 1

#             rpos += 1

#         return ans

# class Solution:
#     def characterReplacement(self, str: str, k: int) -> int:
#         count = {}
#         length = s = 0
#         for f in range(len(str)):

#             count[str[f]] = count.get(str[f], 0) + 1
#             # Move the window
#             while (sum(count.values()) - max(count.values())) > k:
#                 count[str[s]] = count.get(str[s], 0) - 1
#                 s += 1
#             length = max(length, f - s + 1)

#         return length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, maxf, res = 0, 0, 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res

if __name__ == '__main__':
    res = Solution()
    # print(res.characterReplacement("ABAB", 2))
    print(res.characterReplacement("AABABBA", 1))


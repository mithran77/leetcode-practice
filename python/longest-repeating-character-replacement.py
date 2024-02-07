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

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = rpos = lpos = 0
        char_count = {}

        while rpos < len(s):
            r = s[rpos]
            l = s[lpos]

            if r not in char_count:
                char_count[r] = 0
            char_count[r] += 1

            cur_len = rpos - lpos + 1

            if (cur_len - max(char_count.values())) <= k:
                ans = max(ans, cur_len)
            else:
                char_count[l] -= 1
                if char_count[l] == 0:
                    del char_count[l]
                lpos += 1

            rpos += 1

        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.maxArea([1,1]))
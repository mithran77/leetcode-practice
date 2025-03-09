# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len check
        if len(s1) > len(s2):
            return False

        # Get char count of s1
        char_cnt_s1 = defaultdict(int)
        for c in s1:
            char_cnt_s1[c] += 1

        for i in range(len(s2) - len(s1) + 1):
            if s2[i] in char_cnt_s1:
                # Grow till len(s1)
                char_cnt_s2 = defaultdict(int)
                for j in range(len(s1)):
                    char_cnt_s2[s2[i+j]] += 1

                # return True, if char counts are same
                if char_cnt_s2 == char_cnt_s1:
                    return True

        return False


if __name__ == '__main__':
    res = Solution()
    print(res.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
    print(res.checkInclusion(s1 = "ab", s2 = "eidboaoo"))



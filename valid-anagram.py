# 242. Valid Anagram
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         if len(t) != len(s):
#             return False

#         charCount = {}

#         for c in s:
#             if c in charCount.keys():
#                 charCount[c] += 1
#             else:
#                 charCount[c] = 1

#         for c in t:
#             if c in charCount:
#                 if charCount[c] == 0:
#                     return False
#                 else:
#                     charCount[c] -= 1
#             else:
#                 return False

#         if charCount != {}:
#             return False

#         return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_cnt = {}
        
        for c in s:
            s_cnt[c] = s_cnt.get(c, 0) + 1
        
        for c in t:

            s_cnt[c] = s_cnt.get(c, 0) - 1

            if s_cnt[c] < 0:
                return False

            if s_cnt[c] == 0:
                del(s_cnt[c])

        return s_cnt == {}


if __name__ == '__main__':
    res = Solution()
    print(res.isAnagram("anagram", "nagaram"))
from typing import List
import collections
import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # s = re.sub(r'[\W_]+', '', s.lower())
#         l, r = 0, len(s)-1
#         while l < r:
#             if not s[l].isalnum():
#                 l += 1
#                 continue
#             elif not s[r].isalnum():
#                 r -= 1
#                 continue
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1
#         return True

# class Solution:

#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1

#         while l < r:
#             while l < r and not self.isAlphaNum(s[l]):
#                 l += 1
#             while l < r and not self.isAlphaNum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l, r = l+1, r-1

#         return True

#     def isAlphaNum(self, s: str) -> bool:
#         return (
#             ord('A') <= ord(s) <= ord('Z') or
#             ord('a') <= ord(s) <= ord('z') or
#             ord('0') <= ord(s) <= ord('9')
#         )

# Simpler to read/understand than above
class Solution:

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1

        return True

    def isAlphaNum(self, s: str) -> bool:
        return (
            ord('A') <= ord(s) <= ord('Z') or
            ord('a') <= ord(s) <= ord('z') or
            ord('0') <= ord(s) <= ord('9')
        )

if __name__ == '__main__':
    res = Solution()
    # print(res.isPalindrome("A man, a plan, a canal: Panama"))
    # print(res.isPalindrome("race a car"))
    # print(res.isPalindrome(" "))
    print(res.isPalindrome("ab_a"))


# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a  palindrome. Return all possible palindrome partitioning of s.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

from typing import List

# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         partitions = []

#         def backtrack(temp, start):
#             if start == len(s):
#                 partitions.append(temp.copy())
#             else:
#                 for i in range(start, len(s)):
#                     if self.is_palindrome(s, start, i):
#                         temp.append(s[start:i+1])
#                         backtrack(temp, i + 1)
#                         temp.pop()

#         backtrack([], 0)
#         return partitions

#     def is_palindrome(self, s, low, high):
#         while low < high:
#             if s[low] != s[high]:
#                 return False
#             low += 1
#             high -= 1
#         return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        partitons = []

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(start, strings):
            if start == len(s):
                partitons.append(strings.copy())
                return

            for i in range(start, len(s)):
                if is_palindrome(start, i):
                    strings.append(s[start:i+1])
                    backtrack(i+1, strings)
                    strings.pop()

        backtrack(0, [])

        return partitons


if __name__ == '__main__':
    res = Solution()
    print(res.partition(s = "aab"))
    print(res.partition(s = "a"))

    # print(res.isPalindrome(s = "aba"))
    # print(res.isPalindrome(s = ""))
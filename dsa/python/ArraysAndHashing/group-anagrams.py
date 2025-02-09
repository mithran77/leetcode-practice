# 49. Group Anagrams
#
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
from typing import List

# # n2
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         # Base case
#         if len(strs) < 2:
#             return [strs]

#         result = []

#         for str in strs:
#             if len(result) == 0: # First iteration
#                 result.append([str])
#             else:
#                 for res in result:
#                     if Solution.isAnagram(res[0], str):
#                         res.append(str)
#                         break
#                 else:
#                     result.append([str])

#         return result

#     @staticmethod
#     def isAnagram(str1: List[str], str2: List[str]) -> bool: # O(n) time and space

#         char_count = {}

#         if len(str1) != len(str2): return False

#         for c in str1:
#             if c in char_count:
#                 char_count[c] += 1
#             else:
#                 char_count[c] = 1

#         for c in str2:
#             if c in char_count:
#                 if char_count[c] == 0:
#                     return False
#                 else:
#                     char_count[c] -= 1
#             else:
#                 return False

#         return True

# res = Solution()
# # res.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# res.groupAnagrams(["ac","c"])

# # Optimized

# import collections

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         output = collections.defaultdict(list)

#         for str in strs:
#             output[tuple(sorted(str))].append(str)

#         return output.values()


import collections
import array as arr
# array solution
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         word_map = collections.defaultdict(lambda:[])

#         for w in strs:
#             k = arr.array('i',[0] * 26)
#             for c in w:
#                 k[ord(c.lower()) - ord('a')] += 1
#             word_map[str(k)].append(w)

#         return word_map.values()

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = {}

#         for word in strs:
#             cnt = [0] * 26

#             for c in word:
#                 cnt[ord(c) - ord('a')] += 1
    
#             cnt = tuple(cnt)
#             if cnt not in anagrams:
#                 anagrams[cnt] = []

#             anagrams[cnt].append(word)

#         res = []
#         for k in anagrams:
#             res.append(anagrams[k])
#         return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()


if __name__ == '__main__':
    res = Solution()
    print(res.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
    print(res.groupAnagrams(strs = [""]))
    print(res.groupAnagrams(strs = ["a"]))

from typing import List
#
# https://www.lintcode.com/problem/659/
# https://leetcode.com/problems/encode-and-decode-strings/description/
# https://neetcode.io/problems/string-encode-and-decode
#
# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
#
# Please implement encode and decode
#
# Example 1:
#
# Input: ["neet","code","love","you"]
#
# Output:["neet","code","love","you"]
# Example 2:
#
# Input: ["we","say",":","yes"]
#
# Output: ["we","say",":","yes"]
# Constraints:
#
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.
#

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i : j])
            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return res

if __name__ == '__main__':
    ans = Solution()
    print(ans.encode(["neet","code","love","you"]))
    print(ans.decode("4#neet4#code4#love3#you"))
